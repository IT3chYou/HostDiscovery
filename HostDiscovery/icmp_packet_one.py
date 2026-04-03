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



class ICMPone:
    def __init__(self):
        self.pack = Modules()


    def HosDiscoveryOnePackReceive(self, ip_address: str, timeout: int, port_range: int, verbose: bool, port_type,fake_ip_range: int, ip_class, proxy, os: bool):
        print("")
        print("[bold white]Dest Host \t\t\tReply From Host\t\t\tPort Status \t\t\t Protocols \t\t\t Operating System[/bold white]")
        cizgi = 170 * "-"
        print(f"[bold yellow]{cizgi}[/bold yellow]")

        PortNumbers = []
        ProtocolList = []
        SourceIp = ""
        DestIP = ""
        Os = []

        # 1. Proxy Bağlantısı
        if proxy is not None:
            if not  self.pack.proxy_connect(proxy):
                print("[red]Proxy bağlantısı başarısız oldu.[/red]")
                return

        # 2. ADIM: SİS PERDESİ (FAKE IP) - Sadece gürültü yapar, cevap beklemez.
        if fake_ip_range is not None:
            print(f"[yellow][!] {fake_ip_range} adet sahte paket ile sis perdesi oluşturuluyor...[/yellow]")
            for y in range(fake_ip_range):
                # Burada 'port_type' varsa TCP, yoksa ICMP sahte paket atıyoruz
                if port_type is not None:
                    self.pack.tcp_packet_with_scapy(ip_address, ip_class)
                else:
                    self.pack.icmp_packet_with_scapy(ip_address, ip_class)

        # 3. ADIM: GERÇEK PORT TARAMASI - Kendi IP'n ile yapılır, cevaplar listeye girer.
        if port_range is not None and port_type is not None:
            print(f"[blue][*] Gerçek IP ile {port_type} port taraması yapılıyor (1-{port_range})...[/blue]")
            for x in range(1, port_range + 1):
                status = False
                if port_type == "TCP":
                    status = self.pack.PortScannerWithTCP(ip_address, x)
                elif port_type == "UDP":
                    status = self.pack.PortScannerWithUDP(ip_address, x)
                elif port_type == "SYN":
                    status = self.pack.PortScannerWithSYN(ip_address, x)
                elif port_type == "ACK":
                    status = self.pack.PortScannerWithACK(ip_address, x)
                elif port_type == "FIN":
                    status = self.pack.PortScannerWithFIN(ip_address, x)

                if status:
                    PortNumbers.append(x)

        # 4. Protokol Eşleştirme
        for protocol in self.pack.protocols:
            for y in PortNumbers:
                if y == protocol["port"]:
                    ProtocolList.append(protocol["service"])

        # 5. ICMP Kontrolü ve Sonuç Yazdırma
        icmp_packet = scapy.sr1(scapy.IP(dst=ip_address) / scapy.ICMP(), timeout=timeout, verbose=verbose)

        if icmp_packet:
            if os == True:
                Detect = self.pack.Os_Detection(ip_address)
                Os.append(Detect)

            SourceIp = icmp_packet.src
            # Sonucu ekrana bas
            print(f'{ip_address} \t\t\t {SourceIp} \t\t\t {list(PortNumbers)} \t\t\t {list(ProtocolList)} \t\t\t{Os}')
        else:
            print(f"[red]Host {ip_address} is unreachable (No ICMP Reply).[/red]")
