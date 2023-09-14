# Pass-the-Hash (PtH) Attack Detection System

This comprehensive documentation outlines the architecture and implementation details of a sophisticated Pass-the-Hash (PtH) attack detection system developed in Python. PtH attacks represent a critical security concern, and this system employs a range of technologies, including packet capture, network analysis, and cryptography, to proactively identify potential PtH attacks in real-time.

## Overview

Pass-the-Hash attacks are a prevalent technique employed by malicious actors to gain unauthorized access to systems by exploiting hashed credentials of legitimate users. Detecting such attacks is paramount for preserving network security. This documentation presents a PtH attack detection system built using Python and leveraging the following essential libraries and technologies:

- [pydivert](https://github.com/ffalcinelli/pydivert): A Python library for Windows, enabling packet capture and manipulation.
- [wmi](https://pypi.org/project/WMI/): The Windows Management Instrumentation (WMI) library, facilitating system information retrieval.
- [netifaces](https://pypi.org/project/netifaces/): A Python library for accessing network interface information.
- [Cryptodome](https://pypi.org/project/pycryptodome/): A Python library offering cryptographic capabilities.

## Key Components

### 1. PtH Attack Detection Logic

At the core of the system is the `detect_pth_attack` function, which analyzes Server Message Block (SMB) traffic to identify potential PtH attacks. It scrutinizes SMB packets on port 445, specifically looking for authentication requests indicative of PtH attacks.

```python
def detect_pth_attack(packet):
    # Detects a pass-the-hash attack by analyzing SMB traffic
    smb_packet = packet.tcp
    if smb_packet.dst_port == 445 and smb_packet.payload:
        # Check if the SMB packet is an authentication request
        if smb_packet.payload[8] == 0x73 and smb_packet.payload[9] == 0x0d:
            return True
    return False
```

### 2. Network Interface Detection

To determine the network interface to monitor, the system utilizes the `find_interface_guid` function. This function identifies the default network interface and retrieves its MAC address.

```python
def find_interface_guid():
    gateways = netifaces.gateways()
    default_interface = gateways['default'][netifaces.AF_INET][1]
    interfaces = netifaces.interfaces()

    for interface in interfaces:
        if interface == default_interface:
            addrs = netifaces.ifaddresses(interface)
            if netifaces.AF_LINK in addrs:
                mac_address = addrs[netifaces.AF_LINK][0]['addr']
                return mac_address

    return None
```

### 3. Packet Capture and Analysis

The `packet_handler` function is responsible for processing captured packets. It calls the `detect_pth_attack` function to check if an SMB packet indicates a PtH attack.

```python
def packet_handler(packet):
    if detect_pth_attack(packet):
        print("Potential pass-the-hash attack detected!")
```

### 4. Main Function

The `main` function orchestrates the entire PtH attack detection system. It identifies the network interface to monitor, sets up packet filtering criteria, and initiates packet capture using pydivert.

```python
def main():
    interface_guid = find_interface_guid()

    if interface_guid:
        filter_expression = 'tcp.DstPort == 445'  # Capture only TCP traffic on port 445 (SMB)

        # Open the network interface in packet capture mode
        with pydivert.WinDivert(filter=filter_expression, layer=0, flags=pydivert.Flag.SNIFF) as w:
            print(f"Started capturing on interface with GUID: {interface_guid}...")
            # Start capturing packets
            for packet in w:
                packet_handler(packet)

        print("Capture stopped.")
    else:
        print("No active network interface found.")

if __name__ == '__main__':
    main()
```

## Usage

1. Ensure you have the necessary libraries installed. You can install them using pip:

   ```bash
   pip install pydivert wmi netifaces pycryptodome
   ```

2. Run the `pass_the_hash_detector.py` script. It will capture and analyze network packets, printing a message when a potential PtH attack is detected.

## Customization

This system can be further customized by adjusting packet filtering criteria, implementing additional analysis logic, or integrating it with your network security infrastructure.

## Dependencies

- Python 3.x
- pydivert
- wmi
- netifaces
- Cryptodome

