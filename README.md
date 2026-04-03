# 🐍 HostDiscovery

Welcome to **HostDiscovery Program**! 🎯

This script provides information about devices located within the network. ✨

This tool is not as advanced as tools like `nmap`.  
Port detection and service detection have been kept simple and superficial.

---

- 🐍 Python scripts (`.py` files)  
- 📄 Short description and usage documentation  
- ⚙️ Optional requirements or config files  

---

## 🚀 How to Use

Most scripts can be executed directly via the terminal.  
Use `-h` or `--help` to see usage instructions.

```bash
python Hostdiscovery.py -h

python Hostdiscovery.py --type ARP -i 192.168.1.0 -s /24 -c 10 -t 5 -v

python Hostdiscovery.py --type ICMP1Rec -i 192.168.1.1

python Hostdiscovery.py --type ICMP4Rec -i 192.168.1.1 -pt TCP -pr 100 -fi 100 -ic
````

usage: Host_Discovery_Version2.py [-h] --type {ICMP4Rec,ARP,ICMP1Rec}
                                  [-s SUBNET_MASK]
                                  [-i IP_ADDRESS]
                                  [-c COUNT]
                                  [-t TIMEOUT]
                                  [-v]
                                  [-pr PORT_RANGE]
                                  [-pt {TCP,UDP,SYN,ACK,FIN}]
                                  [-fi FAKE_IP]
                                  [-ic IP_CLASS]
                                  [-p PROXY]
                                  [-o]


| Argument                                                                    | Description                                     |
| --------------------------------------------------------------------------- | ----------------------------------------------- |
| `-h, --help`                                                                | Show this help message and exit                 |
| `--type {ICMP4Rec, ARP, ICMP1Rec}`                                          | Choose scan type                                |
| `-s SUBNET_MASK, --subnet_mask SUBNET_MASK`                                 | Specify subnet mask (e.g. `/24`)                |
| `-i IP_ADDRESS, --ip_address IP_ADDRESS`                                    | Target IP address                               |
| `-c COUNT, --count COUNT`                                                   | Number of times to repeat scan                  |
| `-t TIMEOUT, --timeout TIMEOUT`                                             | Response timeout in seconds                     |
| `-v, --verbose`                                                             | Verbose output to show detailed process         |
| `-pr PORT_RANGE, --port_scan PORT_RANGE`                                    | Specify port range for scanning (e.g. `20-100`) |
| `-pt {TCP, UDP, SYN, ACK, FIN}, --port_scan_type {TCP, UDP, SYN, ACK, FIN}` | Specify port scan type                          |
| `-fi FAKE_IP, --fake-ip FAKE_IP`                                            | Use a fake IP address or IP range for scanning  |
| `-ic IP_CLASS, --ip_class IP_CLASS`                                         | Specify IP class                                |
| `-p PROXY, --proxy PROXY`                                                   | Choose specific proxy server or random proxy    |
| `-o, --OS`                                                                  | Attempt to detect Operating System              |



This tool is a lightweight network scanner for quick device discovery.

For in-depth scanning and analysis, consider tools like nmap.

Port scanning types (TCP, UDP, SYN, ACK, FIN) offer different scanning methods for varied use cases.

Use --verbose to get detailed output useful for troubleshooting or understanding scan progress.
