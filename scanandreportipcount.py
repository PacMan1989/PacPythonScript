import os
import socket
from scapy.all import ARP, Ether, srp

def get_network_devices():
    target_ip = "192.168.1.1/24"  # Change this to your network's IP range
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []

    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def list_c_drive():
    return os.listdir('C:\\')

def main():
    devices = get_network_devices()
    c_drive = list_c_drive()

    print(f"Total devices found on the network: {len(devices)}")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")

    print("\nC drive directories:")
    for directory in c_drive:
        print(directory)

if __name__ == "__main__":
    main()
#pip install scapy#
