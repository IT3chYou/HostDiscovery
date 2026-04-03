import scapy.all as scapy
from rich import print
import argparse
import requests
import time
from time import sleep
import socket
import random
import os
from concurrent.futures import ThreadPoolExecutor
from modules_packet  import Modules



class ARP_:
    def __init__(self, iface=None):
        self.iface = iface
        self.time = time.time()
        self.pack = Modules()

    def HostDiscoveryWithArp(self, ip_address: str, subnet_mask: str, count: int, timeout: int, verbose: bool,port_range: int, port_type, fake_ip_range: int, ip_class, proxy, os: bool):
        print("\n[bold white]IP\t\tMAC Adresi \t\tMAC Vendor \t\tPort Status \t Service Name \t\t Operating System[/bold white]")
        cizgi = 170 * "-"
        print(f"[bold yellow]{cizgi}[/bold yellow]")

        # 1. ARP Taraması (Tüm ağı hızlıca tara)
        target_ip = f"{ip_address}{subnet_mask}"  # Örn: 192.168.1.0/24

        # Scapy'nin bazen Windows'ta paket kaçırmaması için inter (gecikme) ekliyoruz
        arp_request_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=target_ip)
        answered_list = \
        scapy.srp(arp_request_broadcast, timeout=timeout, verbose=verbose, iface=self.iface, inter=0.1, retry=2)[0]
        # Paketler arası 100ms boşluk (Windows için kritik)
        # Cevap gelmezse 2 kez daha dene

        if not answered_list:
            print("[red]Ağda aktif cihaz bulunamadı veya yetki sorunu var.[/red]")
            return

        # 2. Port Tarama Yardımcı Fonksiyonu (Thread'ler bunu kullanacak)
        def scan_single_port(ip, port, p_type):
            status = False
            if p_type == "TCP":
                status = self.pack.PortScannerWithTCP(ip, port)
            elif p_type == "SYN":
                status = self.pack.PortScannerWithSYN(ip, port)
            elif p_type == "UDP":
                status = self.pack.PortScannerWithUDP(ip, port)
            elif p_type == "ACK":
                status = self.pack.PortScannerWithACK(ip, port)
            elif p_type == "FIN":
                status = self.pack.PortScannerWithFIN(ip, port)
            return (port, status)

        # 3. Her bulunan cihaz için işlemleri yap
        for element in answered_list:
            found_ip = element[1].psrc
            found_mac = element[1].hwsrc

            current_ports = []
            current_protocols = []
            current_os = "N/A"

            # --- MULTI-THREADED PORT TARAMA ---
            if port_range and port_type:
                with ThreadPoolExecutor(max_workers=50) as executor:
                    # Portları kuyruğa ekle
                    future_to_port = {executor.submit(scan_single_port, found_ip, p, port_type): p for p in
                                      range(1, port_range + 1)}

                    for future in future_to_port:
                        port, is_open = future.result()
                        if is_open:
                            current_ports.append(port)
                            # Protokol ismini bul
                            for proto in self.pack.protocols:
                                if proto["port"] == port:
                                    current_protocols.append(proto["service"])

            # OS Tespiti
            if os:
                current_os = self.pack.Os_Detection(found_ip)

            # Vendor Bilgisi
            vendor_info = self.pack.get_mac_vendor(found_mac)

            # Sonuç Satırı
            print(f"{found_ip}\t{found_mac}\t{vendor_info[:20]}\t{current_ports}\t{current_protocols}\t{current_os}")
