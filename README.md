# 🐍 HostDiscovery

A lightweight network discovery and scanning tool developed with Python and Scapy.

HostDiscovery is designed as a personal networking project to explore:

- ARP-based host discovery
- ICMP-based host discovery
- TCP/UDP port scanning
- SYN, ACK and FIN scanning techniques
- MAC address vendor lookup
- Basic operating system fingerprinting
- Network packet manipulation with Scapy

> ⚠️ HostDiscovery is a personal learning project and is not intended
> to replace mature tools such as Nmap.

## 🚀 Features

### 🔎 Host Discovery
- ARP discovery
- ICMP-based discovery
- IP and MAC address detection

### 🔌 Port Scanning
Supported scan types:

- TCP
- UDP
- SYN
- ACK
- FIN

### 🖥️ Basic OS Detection

Attempts to identify the target operating system using:

- IP TTL
- TCP window size

The result is heuristic and should not be considered definitive.

### 🌐 MAC Vendor Lookup

MAC addresses can be queried to determine the associated vendor.


HostDiscovery
│
├── Host Discovery
│   ├── ARP
│   └── ICMP
│
├── Port Scanning
│   ├── TCP
│   ├── UDP
│   ├── SYN
│   ├── ACK
│   └── FIN
│
├── OS Detection
├── MAC Vendor Lookup
└── Packet Manipulation
