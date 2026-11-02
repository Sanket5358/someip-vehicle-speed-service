# Wireshark and TShark Analysis

## Objective

Capture and inspect network traffic associated with the vehicle speed application.

## Important Note

The preliminary capture file previously created by the project contained zero packets. The instructions below describe how to make a new capture; they do not mean packet-level verification has already succeeded.

## Step 1: Start the Application

Run the daemon, provider, and consumer in separate terminal windows.

Do not start duplicate daemon instances.

## Step 2: Capture Traffic

Open another terminal and run:

    cd ~/someip-vehicle-speed-service
    sudo tshark -i lo -f "udp port 3000 or udp port 3002" -w /tmp/someip_capture.pcapng

While the capture runs, generate application traffic by using the consumer and provider.

Stop the capture with Ctrl+C after traffic has been generated.

If the capture still contains zero packets, investigate whether the application is using the expected ports and whether the traffic is visible on the loopback interface.

## Step 3: Inspect the Packet Count

    sudo capinfos /tmp/someip_capture.pcapng

Check the Number of packets field.

## Step 4: Copy the Capture to the Project

    cd ~/someip-vehicle-speed-service
    sudo cp /tmp/someip_capture.pcapng wireshark/
    sudo chown "$USER":"$(id -gn)" wireshark/someip_capture.pcapng
    chmod 644 wireshark/someip_capture.pcapng

## Step 5: Decode Packets

    tshark -r wireshark/someip_capture.pcapng \
    -d udp.port==3000,someip \
    -d udp.port==3002,someip \
    -Y someip \
    -T fields \
    -e frame.number \
    -e ip.src \
    -e udp.srcport \
    -e ip.dst \
    -e udp.dstport \
    -e someip.serviceid \
    -e someip.methodid \
    -e someip.messagetype \
    -e someip.returncode

If TShark cannot read the file because of permissions, inspect the file and parent-directory permissions. Use sudo for diagnosis if necessary.

## Step 6: What to Verify

### Request

Check for a request from the consumer to the provider with service ID 0x1234 and method ID 0x0001.

### Response

Check for a corresponding response from the provider to the consumer.

### Event

Inspect the event traffic and verify the SpeedChanged event ID 0x8001. Event messages may be represented differently from method messages in the dissector fields.

### Service Discovery

If service-discovery traffic is required, perform a separate capture including UDP port 30490 and inspect the SOME/IP-SD packets.

## Final Evidence

Keep the final capture only after confirming that it contains packets. Record the actual packet count and observed message types in the report.

