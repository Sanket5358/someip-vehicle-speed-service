
"""
Instrument Cluster — SOME/IP Vehicle Speed Consumer.

Features:
1. Connects to the someipyd daemon.
2. Calls the GetSpeed method.
3. Decodes the vehicle speed response.
4. Subscribes to SpeedChanged events.
5. Displays speed updates received from the provider.
"""

import asyncio
import logging

from someipy import (
    ClientServiceInstance,
    connect_to_someipy_daemon,
)
from someipy.someipy_logging import set_someipy_log_level

from vehicle_speed_interface import (
    GET_SPEED_METHOD_ID,
    INSTANCE_ID,
    INTERFACE_IP,
    CONSUMER_PORT,
    SERVICE_ID,
    SPEED_CHANGED_EVENT_ID,
    SpeedPayload,
    speed_eventgroup,
    vehicle_speed_service,
)


def speed_changed_callback(event_id: int, payload: bytes) -> None:
    """Decode and display received SpeedChanged events."""

    if event_id != SPEED_CHANGED_EVENT_ID:
        return

    speed_data = SpeedPayload()
    speed_data.deserialize(payload)

    print(
        f"\n[EVENT] SpeedChanged: "
        f"{speed_data.speed_kmph.value} km/h"
    )


async def main():
    """Run the Instrument Cluster consumer."""

    set_someipy_log_level(logging.INFO)

    daemon = await connect_to_someipy_daemon()

    client = ClientServiceInstance(
        daemon,
        vehicle_speed_service,
        INSTANCE_ID,
        INTERFACE_IP,
        CONSUMER_PORT,
    )

    try:
        print("\n========================================")
        print("  INSTRUMENT CLUSTER - SOME/IP CONSUMER")
        print("========================================")
        print(f"Service ID    : 0x{SERVICE_ID:04X}")
        print(f"Instance ID   : 0x{INSTANCE_ID:04X}")
        print(f"Consumer port : {CONSUMER_PORT}")
        print(f"Provider IP   : {INTERFACE_IP}")

        # Register the callback before subscribing.
        client.register_callback(speed_changed_callback)

        # Give the daemon a moment to initialize the client.
        await asyncio.sleep(1)

        # Request the current vehicle speed.
        print("\n[REQUEST] Sending GetSpeed request...")

        result = await client.call_method(
            GET_SPEED_METHOD_ID,
            b"",
        )

        print(f"[RESPONSE] Message type : {result.message_type}")
        print(f"[RESPONSE] Return code  : {result.return_code}")

        if result.payload:
            speed_data = SpeedPayload()
            speed_data.deserialize(result.payload)

            print(
                f"[RESPONSE] Vehicle speed: "
                f"{speed_data.speed_kmph.value} km/h"
            )
        else:
            print("[WARNING] The response contains no speed payload.")

        # Subscribe to SpeedChanged events.
        print("\n[SUBSCRIBE] Requesting SpeedChanged events...")

        client.subscribe_eventgroup(
            speed_eventgroup,
            ttl_subscription_seconds=30,
        )

        print("[SUBSCRIBE] Subscription request sent.")
        print("[INFO] Waiting for speed updates. Press Ctrl+C to stop.")

        while True:
            await asyncio.sleep(1)

    finally:
        await daemon.disconnect_from_daemon()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nInstrument Cluster consumer stopped.")

