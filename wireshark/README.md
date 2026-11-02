# Wireshark Evidence

Store verified SOME/IP packet captures in this directory.

Recommended final filename:

    someip_vehicle_speed_final.pcapng

Before treating a capture as final, check its packet count:

    capinfos someip_vehicle_speed_final.pcapng

A capture with zero packets is not sufficient evidence of communication.

The preliminary file someip_vehicle_speed_final.pcapng previously contained zero packets. Replace it only after successfully capturing and verifying real traffic.

Useful packet fields include:

- Frame number
- Source and destination IP addresses
- Source and destination UDP ports
- SOME/IP service ID
- SOME/IP method or event ID
- SOME/IP message type
- Return code, where applicable

