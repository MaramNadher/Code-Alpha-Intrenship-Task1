import socket
import struct

# Create raw socket to capture packets
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

while True:
    raw_data, addr = sniffer.recvfrom(65535)
    dest_mac, src_mac, eth_proto = struct.unpack('!6s6sH', raw_data[:14])

    print('\nEthernet Frame:')
    print(f'Destination MAC: {":".join(format(b, "02x") for b in dest_mac)}')
    print(f'Source MAC: {":".join(format(b, "02x") for b in src_mac)}')
    print(f'Protocol: {eth_proto}')
