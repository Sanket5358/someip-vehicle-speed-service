# System Architecture

## 1. Overview

The project demonstrates vehicle speed communication using a SOME/IP provider and consumer running on Ubuntu Linux.

## 2. Logical Architecture

                 +---------------------------+
                 | Instrument Cluster        |
                 | Consumer                  |
                 |                           |
                 | GetSpeed Request          |
                 | SpeedChanged Subscription |
                 +-------------+-------------+
                               |
                               |
                      SOME/IP over UDP
                      Localhost Interface
                               |
                 +-------------v-------------+
                 | Vehicle Speed             |
                 | Service Provider          |
                 |                           |
                 | GetSpeed Response         |
                 | SpeedChanged Events       |
                 +---------------------------+

                 +---------------------------+
                 | someipyd Daemon           |
                 | SOME/IP Communication     |
                 | Infrastructure            |
                 +---------------------------+

The diagram is a logical representation. It does not indicate that all application messages pass through the daemon as ordinary application payloads.

## 3. Main Components

### Consumer

Requests the current vehicle speed and subscribes to speed-change notifications.

### Provider

Responds to GetSpeed requests and publishes speed-change events.

### Interface Module

Defines the service interface used by the Python application.

### Daemon

Provides the SOME/IP communication infrastructure used by the project.

### Packet Analyzer

Wireshark/TShark can be used to capture and inspect network traffic.

## 4. Configured Identifiers

| Item | Configured Value |
|---|---|
| Service ID | 0x1234 |
| Instance ID | 0x5678 |
| Method ID | 0x0001 |
| Event ID | 0x8001 |
| Event Group ID | 0x0001 |
| Provider | 127.0.0.1:3000 |
| Consumer | UDP port 3002 |
| SD multicast | 224.224.224.245:30490 |

## 5. GetSpeed Sequence

1. The consumer sends a request.
2. The provider receives and processes the request.
3. The provider prepares the speed response.
4. The response is returned to the consumer.
5. The consumer displays the speed.

## 6. Event Sequence

1. The consumer requests a subscription.
2. The provider publishes speed updates.
3. The consumer receives notifications.
4. The displayed speed is updated.

The exact subscription and event-delivery behaviour should be verified using the application's logs and a packet capture.

