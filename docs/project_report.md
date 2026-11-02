# SOME/IP-Based Vehicle Speed Monitoring System

## 1. Introduction

Modern vehicles contain multiple Electronic Control Units (ECUs) that exchange information to perform functions such as engine management, instrument display, diagnostics, and vehicle monitoring.

Service-Oriented Middleware over IP (SOME/IP) enables service-based communication between automotive applications. It supports request-response communication and event-based notifications.

This project implements a vehicle speed monitoring application using Python and the someipy library. A Vehicle Speed Service Provider supplies vehicle speed information, while an Instrument Cluster Consumer requests the current speed and receives speed-change notifications.

## 2. Problem Statement

Automotive applications require a structured mechanism to exchange data between software components. The project demonstrates how a vehicle speed service can provide information to a consumer through SOME/IP communication.

## 3. Objectives

- Understand SOME/IP service-oriented communication.
- Implement a Vehicle Speed Service Provider in Python.
- Implement an Instrument Cluster Consumer.
- Demonstrate GetSpeed request-response communication.
- Demonstrate SpeedChanged event notifications.
- Configure the SOME/IP daemon.
- Inspect network traffic using Wireshark and TShark.
- Document the implementation and testing procedure.

## 4. System Architecture

The system contains the following components:

1. Vehicle Speed Service Provider
2. Instrument Cluster Consumer
3. SOME/IP interface definitions
4. someipyd daemon
5. Loopback network interface
6. Wireshark/TShark packet analysis tools

The provider supplies vehicle speed information. The consumer requests the current speed and subscribes to speed-change events.

The daemon supports the SOME/IP communication infrastructure used by the application.

## 5. Hardware and Software Requirements

### Software

- Ubuntu Linux
- Python 3
- Python virtual environment
- someipy Python package
- someipyd daemon
- Wireshark or TShark
- Terminal

### Hardware

A computer capable of running Ubuntu Linux is sufficient for this software-based demonstration.

No physical automotive ECU or vehicle is required for the current loopback-based implementation.

## 6. Project Configuration

The current project configuration uses the following identifiers:

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
| SOME/IP-SD Multicast Address | 224.224.224.245 |
| SOME/IP-SD Port | 30490 |

These are the project's configured values. Confirm the source files before changing the configuration.

## 7. Implementation

### 7.1 Interface Definition

File: `src/vehicle_speed_interface.py`

This file contains the interface definitions used by the provider and consumer.

### 7.2 Service Provider

File: `src/vehicle_speed_service.py`

The provider supplies vehicle speed information and publishes SpeedChanged notifications.

The provider has been observed starting successfully and logging speed updates. Terminal testing also showed a GetSpeed request being received and a response being generated.

### 7.3 Consumer

File: `src/vehicle_speed_consumer.py`

The consumer requests the current vehicle speed and subscribes to SpeedChanged notifications.

During previous terminal testing, the consumer received a successful GetSpeed response and displayed subsequent speed updates.

### 7.4 Speed Simulator

File: `src/speed_simulator.py`

This file is present in the project. Its exact behaviour should be confirmed by inspecting the implementation before describing it as an independently verified component.

### 7.5 SOME/IP Daemon

Configuration file: `config/someipyd.json`

The daemon provides the communication infrastructure required by the application.

## 8. Communication Workflow

### GetSpeed Request and Response

1. The consumer sends a GetSpeed request.
2. The provider receives the request.
3. The provider obtains the current simulated speed.
4. The provider sends a response containing the speed.
5. The consumer displays the returned value.

### SpeedChanged Events

1. The consumer requests an event subscription.
2. The provider publishes speed-change notifications.
3. The consumer receives event notifications.
4. The consumer displays the updated speed.

The event workflow was observed in application terminal logs. Packet-level verification remains pending.

## 9. Execution Procedure

Open separate terminal windows.

### Terminal 1: Start the daemon

    cd ~/someip-vehicle-speed-service
    source .venv/bin/activate
    someipyd --config config/someipyd.json

If the daemon is already running, do not start another instance.

### Terminal 2: Start the provider

    cd ~/someip-vehicle-speed-service
    source .venv/bin/activate
    python src/vehicle_speed_service.py

### Terminal 3: Start the consumer

    cd ~/someip-vehicle-speed-service
    source .venv/bin/activate
    python src/vehicle_speed_consumer.py

The application has previously been tested using these commands.

## 10. Testing and Results

### Test 1: Daemon Startup

Observed result: The daemon started and reported that its Unix domain socket server was running.

Status: Passed in previous testing.

### Test 2: Provider Startup

Observed result: The provider started and reported its service ID, instance ID, and endpoint.

Status: Passed in previous testing.

### Test 3: GetSpeed Request and Response

Observed result: The consumer received a response with return code E_OK and displayed the returned vehicle speed.

Status: Passed in previous testing.

### Test 4: SpeedChanged Event Notifications

Observed result: The consumer displayed multiple speed-change notifications.

Status: Passed at the application level in previous testing.

### Test 5: Packet Capture

A preliminary TShark capture file was created, but its reported packet count was zero.

Status: Pending. A successful packet capture and packet-level analysis are still required.

## 11. Limitations

- The current demonstration uses localhost communication.
- The speed values are simulated rather than obtained from a physical vehicle.
- Physical ECU integration has not been established.
- Packet-level verification is not complete.
- Production automotive security, authentication, and fault handling are outside the current demonstrated scope.

## 12. Future Scope

- Integrate physical ECUs or embedded development boards.
- Add a graphical instrument cluster.
- Add diagnostic services.
- Test communication between separate computers.
- Add stronger error handling and connection monitoring.
- Capture and analyze actual SOME/IP request, response, and event packets.
- Evaluate communication behaviour under packet loss and network load.

## 13. Conclusion

This project demonstrates the implementation of a Python-based vehicle speed monitoring application using SOME/IP concepts. The provider and consumer have demonstrated request-response communication and event notifications at the application level.

The remaining verification task is to capture and inspect the corresponding network packets. The project provides a foundation for further experimentation with automotive service-oriented communication.

