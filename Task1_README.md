# Task 1: Network Packet Sniffer

This Python script captures Ethernet frames using a raw socket.

## How to Run
This must be run with sudo/admin privileges:
```
sudo python3 sniffer.py
```

Use a separate terminal to run:
```
ping google.com
```

You will see live frame output showing MAC addresses and protocol.

## Requirements
- Python 3
- Linux OS (with AF_PACKET support)

## Note
If you're testing in an online compiler or restricted system, raw sockets won't work.
