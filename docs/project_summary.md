# Project Summary

## Title

SOME/IP-Based Vehicle Speed Monitoring System

## Abstract

This project demonstrates a vehicle speed monitoring application based on SOME/IP (Scalable service-Oriented MiddlewarE over IP). The application is implemented in Python using the someipy library and consists of a Vehicle Speed Service Provider and an Instrument Cluster Consumer.

The provider offers a GetSpeed request-response method and publishes SpeedChanged event notifications. The consumer requests the current speed and subscribes to speed updates. A SOME/IP daemon provides the communication infrastructure, while Wireshark/TShark can be used to analyze network traffic.

Previous application tests showed a successful GetSpeed response and event notifications received by the consumer. Final packet-level verification remains to be completed.

## Objectives

- Implement a SOME/IP provider and consumer.
- Demonstrate request-response communication.
- Demonstrate event-based notifications.
- Configure the SOME/IP daemon.
- Inspect network messages using packet analysis tools.

## Technologies Used

- Python
- someipy
- someipyd
- Ubuntu Linux
- Wireshark/TShark

## Applications

The concepts demonstrated by this project are relevant to learning about automotive middleware, service-oriented communication, ECU software interfaces, and network debugging.

## Conclusion

The project demonstrates the core application-level workflow of a SOME/IP vehicle speed service. The next verification step is to capture actual network packets and confirm the corresponding requests, responses, and events.

