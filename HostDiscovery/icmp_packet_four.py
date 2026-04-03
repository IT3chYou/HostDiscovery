from asyncio import timeout
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


class ICMPfour:
    def __init__(self):
        self.timeout = timeout
        self.pack = Modules()

    def HostDiscoveryWithIcmpFourPackReceive(self, ip_address: str, timeout: int, port_range: int, verbose: bool,port_type, fake_ip_range: int, ip_class, proxy, os: bool):
        print("\n[bold white]Dest Host \t\tReply From Host\t\tPort Status \t\t Protocols \t\t Operating System[/bold white]")
        print(170 * "-")

        PortNumbers = []
        ProtocolList = []

        # 1. Proxy Bağlantısı
        if proxy is not None:
            if not self.pack.proxy_connect(proxy):
                print("[red]Proxy bağlantısı başarısız oldu.[/red]")
                return

        # 2. ADIM: SİS PERDESİ (FAKE IP) - SADECE GÖNDER VE GEÇ
        # Burada 'elif' yerine bağımsız bir 'if' kullanıyoruz ki her zaman çalışabilsin.
        if fake_ip_range is not None:
            print(f"[yellow][!] {fake_ip_range} adet sahte paket fırlatılıyor...[/yellow]")
            for y in range(fake_ip_range):
                if port_type is not None:
                    # Port tipi varsa TCP tabanlı sahte paket
                    self.pack.tcp_packet_with_scapy(ip_address, ip_class)
                else:
                    # Port tipi yoksa ICMP tabanlı sahte paket
                    self.pack.icmp_packet_with_scapy(ip_address, ip_class)

        # 3. ADIM: GERÇEK PORT TARAMASI (CEVAP BEKLEDİĞİMİZ KISIM)
        # Bu blok artık yukarıdaki sahte paketlerden bağımsız çalışır.
        if port_range is not None and port_type is not None:
            print(f"[blue][*] Gerçek IP ile {port_type} port taraması yapılıyor...[/blue]")
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

        # 5. ICMP Tarama ve Çıktı
        # Burası 4 paket gönderip cevap bekleyen kısım
        send_and_receive = scapy.sr(scapy.IP(dst=ip_address) / scapy.ICMP(), timeout=timeout, verbose=verbose)
        answered, unanswered = send_and_receive

        if answered:
            for snd, rcv in answered:
                if rcv.src != '127.0.0.1':
                    current_os = []
                    if os:
                        detect = self.pack.Os_Detection(rcv.src)
                        current_os.append(detect)

                    print(f"{snd.dst} \t\t{rcv.src} \t\t{list(PortNumbers)} \t\t {ProtocolList} \t\t {current_os}")

        if not answered:
            print(f"[red]Host {ip_address} is unreachable.[/red]")
