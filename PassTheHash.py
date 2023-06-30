import pydivert
import wmi
import netifaces
from Cryptodome.Hash import HMAC, MD5

def detect_pth_attack(packet):
    # Detects a pass-the-hash attack by analyzing SMB traffic
    smb_packet = packet.tcp
    if smb_packet.dst_port == 445 and smb_packet.payload:
        # Check if the SMB packet is an authentication request
        if smb_packet.payload[8] == 0x73 and smb_packet.payload[9] == 0x0d:
            return True
    return False

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

def packet_handler(packet):
    if detect_pth_attack(packet):
        print("Potential pass-the-hash attack detected!")

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
