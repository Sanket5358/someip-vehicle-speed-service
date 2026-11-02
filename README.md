# SOME/IP-Based Vehicle Speed Monitoring System

## Project Overview

This project demonstrates a vehicle speed monitoring application using SOME/IP (Scalable service-Oriented MiddlewarE over IP). It contains a Vehicle Speed Service Provider and an Instrument Cluster Consumer implemented in Python using the someipy library.

The provider offers a GetSpeed method and publishes SpeedChanged event notifications. The consumer requests the current speed and subscribes to speed updates.

## Objectives

- Understand SOME/IP service-oriented communication.
- Implement provider and consumer applications.
- Demonstrate request-response communication.
- Demonstrate event-based notifications.
- Inspect network traffic using Wireshark/TShark.

## Technologies

- Ubuntu Linux
- Python 3
- someipy
- someipyd
- Wireshark/TShark

## Project Structure

    someip-vehicle-speed-service/
    ├── config/
    │   └── someipyd.json
    ├── docs/
    │   ├── project_report.md
    │   ├── system_architecture.md
    │   ├── test_cases.md
    │   ├── wireshark_analysis.md
    │   └── project_summary.md
    ├── screenshots/
    │   └── README.md
    ├── src/
    │   ├── speed_simulator.py
    │   ├── vehicle_speed_consumer.py
    │   ├── vehicle_speed_interface.py
    │   └── vehicle_speed_service.py
    ├── wireshark/
    │   └── README.md
    └── README.md

## Configured Service Information

| Parameter | Value |
|---|---|
| Service ID | 0x1234 |
| Instance ID | 0x5678 |
| Major Version | 1 |
| GetSpeed Method ID | 0x0001 |
| SpeedChanged Event ID | 0x8001 |
| Event Group ID | 0x0001 |
| Provider IP | 127.0.0.1 |
| Provider UDP Port | 3000 |
| Consumer UDP Port | 3002 |
| SD Multicast Address | 224.224.224.245 |
| SD Port | 30490 |

## Setup and Execution

Activate the project's virtual environment before running the Python applications.

### Terminal 1: Daemon

    cd ~/someip-vehicle-speed-service
    source .venv/bin/activate
    someipyd --config config/someipyd.json

Do not start a duplicate daemon if one is already running.

### Terminal 2: Provider

    cd ~/someip-vehicle-speed-service
    source .venv/bin/activate
    python src/vehicle_speed_service.py

### Terminal 3: Consumer

    cd ~/someip-vehicle-speed-service
    source .venv/bin/activate
    python src/vehicle_speed_consumer.py

## Communication Workflow

### GetSpeed

1. The consumer sends a GetSpeed request.
2. The provider processes the request.
3. The provider returns the current speed.
4. The consumer displays the response.

### SpeedChanged

1. The consumer requests an event subscription.
2. The provider publishes speed updates.
3. The consumer receives and displays event notifications.

## Testing Status

Application-level request-response communication and event notifications were observed in previous terminal tests.

The preliminary Wireshark/TShark capture contained zero packets. Final packet-level verification remains pending. See `docs/wireshark_analysis.md`.

## Documentation

- `docs/project_report.md` — Detailed report
- `docs/system_architecture.md` — Architecture and communication flow
- `docs/test_cases.md` — Testing procedures and status
- `docs/wireshark_analysis.md` — Packet capture guide
- `docs/project_summary.md` — Abstract, objectives, and conclusion

## Limitations

- Current application testing uses localhost.
- Vehicle speed is simulated.
- Physical ECU integration has not been demonstrated.
- Final network packet verification is pending.

## Future Improvements

- Integrate physical ECUs.
- Add a graphical instrument cluster.
- Add diagnostics and error handling.
- Test communication between separate computers.
- Capture and verify request, response, event, and service-discovery packets.

## Conclusion

The project demonstrates application-level SOME/IP vehicle speed communication using Python. Final packet capture and verification are required to complete the network-analysis evidence.

