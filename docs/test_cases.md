# Test Cases and Results

## Test Environment

- Operating system: Ubuntu Linux
- Language: Python
- Library: someipy
- Daemon: someipyd
- Packet analyzer: TShark/Wireshark
- Network interface: loopback (lo)

## Test Case 1: Daemon Startup

Objective:
Verify that the SOME/IP daemon starts.

Procedure:
1. Activate the virtual environment.
2. Start someipyd using config/someipyd.json.
3. Inspect the terminal output.

Expected result:
The daemon starts and reports its socket server status.

Recorded status:
Passed during previous testing.

## Test Case 2: Provider Startup

Objective:
Verify that the vehicle speed provider starts.

Procedure:
1. Start src/vehicle_speed_service.py.
2. Inspect the provider output.

Expected result:
The provider displays its service configuration and speed updates.

Recorded status:
Passed during previous testing.

## Test Case 3: GetSpeed Request

Objective:
Verify that the consumer requests the current speed.

Procedure:
1. Start the consumer.
2. Observe the GetSpeed request.
3. Check the response and return code.

Expected result:
The consumer receives a successful response and displays a speed value.

Recorded status:
Passed during previous testing.

## Test Case 4: SpeedChanged Notifications

Objective:
Verify application-level event reception.

Procedure:
1. Start the provider.
2. Start the consumer.
3. Observe the subscription output.
4. Check for speed-change notifications.

Expected result:
The consumer displays received speed updates.

Recorded status:
Passed at the application level during previous testing.

## Test Case 5: Packet Capture

Objective:
Capture SOME/IP traffic on the loopback interface.

Procedure:
1. Start the provider and consumer.
2. Start TShark on interface lo.
3. Generate application traffic.
4. Stop the capture.
5. inspect the packet count.

Expected result:
The capture contains relevant packets.

Recorded status:
Pending. The preliminary capture contained zero packets.

## Test Case 6: Packet Decode

Objective:
Decode the captured packets as SOME/IP.

Procedure:
1. Open the capture in TShark or Wireshark.
2. Apply the appropriate SOME/IP decode settings if necessary.
3. Inspect service ID, method ID, message type, and payload.

Expected result:
The request, response, and relevant event traffic can be identified.

Recorded status:
Pending final capture.

## Test Evidence

Save genuine terminal screenshots and packet-capture evidence in the project's screenshots/ and wireshark/ directories.

Do not mark a test as passed until its expected result has been observed.

