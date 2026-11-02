
"""
Virtual Vehicle ECU — SOME/IP Vehicle Speed Service Provider.

Features:
1. Offers the VehicleSpeedService.
2. Responds to GetSpeed requests.
3. Simulates varying vehicle speeds.
4. Publishes SpeedChanged events every five seconds.
"""

import asyncio
import logging

from someipy import (
    MessageType,
    Method,
    MethodResult,
    ReturnCode,
    ServerServiceInstance,
    ServiceBuilder,
    TransportLayerProtocol,
    connect_to_someipy_daemon,
)
from someipy.someipy_logging import set_someipy_log_level

from vehicle_speed_interface import (
    GET_SPEED_METHOD_ID,
    INSTANCE_ID,
    INTERFACE_IP,
    MAJOR_VERSION,
    PROVIDER_PORT,
    SERVICE_ID,
    SPEED_CHANGED_EVENT_ID,
    SPEED_EVENTGROUP_ID,
    SpeedPayload,
    speed_eventgroup,
)

from speed_simulator import get_speed_for_step


# Initial vehicle speed
current_speed_kmph = 0


def get_speed_handler(input_data: bytes, client_address: tuple) -> MethodResult:
    """Respond to GetSpeed with the current vehicle speed."""

    print("\nGetSpeed request received")
    print(f"Consumer address: {client_address[0]}:{client_address[1]}")
    print(f"Current speed: {current_speed_kmph} km/h")

    result = MethodResult()
    result.message_type = MessageType.RESPONSE
    result.return_code = ReturnCode.E_OK
    result.payload = SpeedPayload(current_speed_kmph).serialize()

    print(f"Response payload: {result.payload.hex(' ')}")

    return result


async def main():
    global current_speed_kmph

    set_someipy_log_level(logging.INFO)

    daemon = await connect_to_someipy_daemon()

    # Define the GetSpeed method.
    get_speed_method = Method(
        id=GET_SPEED_METHOD_ID,
        protocol=TransportLayerProtocol.UDP,
        method_handler=get_speed_handler,
    )

    # Build the Vehicle Speed service.
    service = (
        ServiceBuilder()
        .with_service_id(SERVICE_ID)
        .with_major_version(MAJOR_VERSION)
        .with_method(get_speed_method)
        .with_eventgroup(speed_eventgroup)
        .build()
    )

    # Create the provider instance.
    server = ServerServiceInstance(
        daemon,
        service,
        INSTANCE_ID,
        INTERFACE_IP,
        PROVIDER_PORT,
    )

    try:
        # Offer the service.
        await server.start_offer()

        print("\nVehicle Speed Service Provider is running")
        print(f"Service ID: 0x{SERVICE_ID:04X}")
        print(f"Instance ID: 0x{INSTANCE_ID:04X}")
        print(f"Provider endpoint: {INTERFACE_IP}:{PROVIDER_PORT}")
        print(f"SpeedChanged Event ID: 0x{SPEED_CHANGED_EVENT_ID:04X}")
        print(f"Event Group ID: 0x{SPEED_EVENTGROUP_ID:04X}")

        step = 0

        while True:
            # Update the simulated vehicle speed.
            current_speed_kmph = get_speed_for_step(step)

            print(f"\nVehicle speed updated: {current_speed_kmph} km/h")

            # Serialize the current speed into a SOME/IP payload.
            event_payload = SpeedPayload(current_speed_kmph).serialize()

            # Publish the SpeedChanged event.
            server.send_event(
                SPEED_EVENTGROUP_ID,
                SPEED_CHANGED_EVENT_ID,
                event_payload,
            )

            print(
                f"SpeedChanged event published: "
                f"{current_speed_kmph} km/h"
            )

            step += 1

            # Update and publish the next speed after five seconds.
            await asyncio.sleep(5)

    finally:
        await server.stop_offer()
        await daemon.disconnect_from_daemon()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nVehicle Speed Service Provider stopped.")

