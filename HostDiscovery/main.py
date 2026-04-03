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
from arp_packet import ARP_
from icmp_packet_four import ICMPfour
from icmp_packet_one import ICMPone
from modules_packet import Modules


class NetHunter:
    def __init__(self, iface=None) -> None:
        self.iface = iface
        self.time = time.time()
        self.icmp_one = ICMPone()
        self.icmp_four = ICMPfour()
        self.arp = ARP_(iface=self.iface)   # <-- burası önemli
        self.pack = Modules()


    def run(self):
        self.pack.play_police_animation()
        args = self.pack.ParserHostDiscovery()
        if args.type == 'ARP':
            self.arp.HostDiscoveryWithArp(args.ip_address, args.subnet_mask, args.count, args.timeout, args.verbose, args.port_range,args.port_type, args.fake_ip, args.ip_class, args.proxy, args.os)

        elif args.type == 'ICMP4Rec':
            self.icmp_one.HostDiscoveryWithIcmpFourPackReceive(args.ip_address, args.timeout, args.port_range, args.verbose,args.port_type, args.fake_ip, args.ip_class, args.proxy, args.os)
        elif args.type == 'ICMP1Rec':
            self.icmp_four.HosDiscoveryOnePackReceive(args.ip_address, args.timeout, args.port_range, args.verbose, args.port_type,args.fake_ip, args.ip_class, args.proxy, args.os)
        else:
            print("Please choose a valid option.")



if __name__ == "__main__":
    net = NetHunter()
    net.run()


    
    


	
