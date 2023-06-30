# Pass-the-Hash Attack Detector

This is a Python script that detects potential pass-the-hash (PtH) attacks by analyzing Server Message Block (SMB) traffic. The script uses the `pydivert` library to capture network packets, `wmi` to retrieve network interface information, `netifaces` to obtain the default network interface, and `Cryptodome` for cryptographic operations.

## Prerequisites

To run this code on your computer, you need to have the following:

- Python 3.x installed
- `pydivert` library installed (`pip install pydivert`)
- `wmi` library installed (`pip install wmi`)
- `netifaces` library installed (`pip install netifaces`)
- `Cryptodome` library installed (`pip install pycryptodomex`)

## How it works

1. The script defines a function `detect_pth_attack(packet)` to detect pass-the-hash attacks by analyzing SMB traffic. It checks if the packet is an SMB authentication request.
2. The function `find_interface_guid()` retrieves the default network interface's MAC address using the `netifaces` library.
3. The `packet_handler(packet)` function is responsible for handling captured packets. It calls the `detect_pth_attack()` function and prints a message if a potential pass-the-hash attack is detected.
4. The `main()` function is the entry point of the script. It retrieves the interface GUID using `find_interface_guid()` and sets up a packet capture filter for TCP traffic on port 445 (SMB).
5. The script starts capturing packets using `pydivert.WinDivert` and iterates over the captured packets, calling `packet_handler()` for each packet.
6. Finally, the script prints a message when the capture is stopped or if no active network interface is found.

## Running the code

1. Make sure you have met the prerequisites mentioned above.
2. Save the code to a file named `pth_attack_detector.py`.
3. Open a terminal or command prompt and navigate to the directory where the file is located.
4. Run the script by executing the command `python pth_attack_detector.py`.
5. The script will start capturing packets and display a message when a potential pass-the-hash attack is detected.
6. To stop the script, press `Ctrl+C`.

**Note:** This script requires administrative privileges to capture network packets. Make sure to run it with appropriate permissions.

Feel free to modify the script or integrate it into your existing projects to enhance the security of your network environment.
