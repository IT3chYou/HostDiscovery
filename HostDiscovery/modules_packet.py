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



class Modules:
    def __init__(self)->None:
        pass

    # FONKSİYONLAR BURADA, INIT DIŞINDA OLMALI
    def get_internal_ip(self):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                ip = s.getsockname()[0]
                s.close()
                return ip
            except:
                return "127.0.0.1"

    def get_scapy_iface(self):
            import scapy.all as scapy
            try:
                # Scapy'nin kendi içindeki conf.iface her zaman doğruyu vermez
                # Bu yüzden route tablosuna bakmak en garanti "başka yoldur"
                return scapy.conf.route.route("8.8.8.8")[0]
            except Exception as e:
                print(f"Arayüz hatası: {e}")
                return None

    def play_police_animation(self):
            # Renkli ASCII karakterler
            blue = "\033[94m"  # Mavi
            red = "\033[91m"  # Kırmızı
            reset = "\033[0m"  # Renk sıfırlama

            # Animasyon kareleri
            frames = [
                "▓▒░░░░░░░░░░░░░░░░░░░░",
                "▓▓▒░░░░░░░░░░░░░░░░░░░",
                "▓▓▓▒░░░░░░░░░░░░░░░░░░",
                "▓▓▓▓▒░░░░░░░░░░░░░░░░░",
                "▓▓▓▓▓▒░░░░░░░░░░░░░░░░",
                "▓▓▓▓▓▓▒░░░░░░░░░░░░░░░",
                "▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░",
                "▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░",
                "▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░",
                "▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░",
                "▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░",
                "▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░",
                "▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░",
                "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░",
                "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░",
                "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░",
                "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░",
                "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░",
                "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░",
                "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░",
                "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒",
                "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
            ]

            # Ekranı temizleme fonksiyonu
            def clear_console():
                os.system('cls' if os.name == 'nt' else 'clear')

            # Animasyonu oynatma
            for frame in frames:
                clear_console()

                # Kırmızı siren solda, mavi siren sağda
                print(" " * 10 + red + frame + reset + " " * 10 + blue + frame + reset)

                # ASCII arabalar yan yana
                print(
                    "\n" + " " * 6 + red + "    ____          ____    " + reset + "     " + blue + "    ____          ____    " + reset)
                print(
                    " " * 6 + red + "  _/__|__\\____  _/__|__\\____ " + reset + "     " + blue + "  _/__|__\\____  _/__|__\\____ " + reset)
                print(
                    " " * 6 + red + " |  _     _   ||  _     _   |" + reset + "     " + blue + " |  _     _   ||  _     _   |" + reset)
                print(
                    " " * 6 + red + " '-(_)-------(_)-' -(_)-------(_)-" + reset + "     " + blue + " '-(_)-------(_)-' -(_)-------(_)-" + reset)

                time.sleep(0.1)

            # Renkleri değiştirerek ikinci geçiş
            for frame in frames:
                clear_console()

                # Mavi siren solda, kırmızı siren sağda
                print(" " * 10 + blue + frame + reset + " " * 10 + red + frame + reset)

                # ASCII arabalar yan yana
                print(
                    "\n" + " " * 6 + blue + "    ____          ____    " + reset + "     " + red + "    ____          ____    " + reset)
                print(
                    " " * 6 + blue + "  _/__|__\\____  _/__|__\\____ " + reset + "     " + red + "  _/__|__\\____  _/__|__\\____ " + reset)
                print(
                    " " * 6 + blue + " |  _     _   ||  _     _   |" + reset + "     " + red + " |  _     _   ||  _     _   |" + reset)
                print(
                    " " * 6 + blue + " '-(_)-------(_)-' -(_)-------(_)-" + reset + "     " + red + " '-(_)-------(_)-' -(_)-------(_)-" + reset)

                time.sleep(0.1)

    def ParserHostDiscovery(self):
            Parser = argparse.ArgumentParser(description='HostDiscovery')
            Parser.add_argument('--type', dest='type', help='ICMP4Rec, ARP ,ICMP1Rec',
                                choices=['ICMP4Rec', 'ARP', 'ICMP1Rec'], required=True)
            Parser.add_argument('-s', '--subnet_mask', help='Give Subnet Mask With (/)', dest='subnet_mask', type=str)
            Parser.add_argument('-i', '--ip_address', help='Give IP Address', dest='ip_address', type=str)
            Parser.add_argument('-c', '--count', help='How Many Times Do You Repeat It', dest='count', type=int, default=1)
            Parser.add_argument('-t', '--timeout', default=1, dest='timeout', type=int, help='Give Response Time')
            Parser.add_argument('-v', '--verbose', help='Let\'s See What Happened', dest='verbose', action='store_true')
            Parser.add_argument('-pr', '--port_scan', help='Give Port Range', dest='port_range', type=int, default=None)
            Parser.add_argument('-pt', '--port_scan_type', help='Give the Port Scan Type', dest='port_type', type=str,
                                choices=['TCP', 'UDP', 'SYN', 'ACK', 'FIN'], default=None)
            # Parser.add_argument('-a', '--attribute', help='This Will Help You About Scanning', default=None, dest='attribute')
            Parser.add_argument('-fi', '--fake-ip', help='Scan With Fake İp Give a Random Ip Range', dest='fake_ip',
                                default=None, type=int)
            Parser.add_argument('-ic', '--ip_class', help='Please Select İp Class', default=None, dest='ip_class')
            Parser.add_argument('-p', '--proxy', help='Chose Spesific your own proxy server or random option', dest='proxy',
                                default=None)
            Parser.add_argument('-o', '--OS', help='Find Operating System', default=None, dest='os', action='store_true')
            args = Parser.parse_args()
            return args

    def Learn_Window_Size_With_SYN_Packet(self,ip_address):
            ports = [80, 443, 22, 21, 23, 53, 445]
            for dst_port in ports:
                src_port = random.randint(1024, 65535)
                ip_layer = scapy.IP(dst=ip_address)
                tcp_layer = scapy.TCP(sport=src_port, dport=dst_port, flags='S', seq=1000)
                packet = ip_layer / tcp_layer

                try:
                    response = scapy.sr1(packet, timeout=2, verbose=False)
                    if response and response.haslayer(scapy.TCP):
                        tcp_resp = response.getlayer(scapy.TCP)
                        window_size = tcp_resp.window

                        if tcp_resp.flags == 0x14:
                            continue
                        elif tcp_resp.flags == 0x12:
                            # print(f"[snow][ ✔ ] Window Size : {window_size} [/snow]")
                            return window_size
                except PermissionError:
                    print("[red]Yönetici olarak çalıştırmalısın![/red]")
                except Exception as e:
                    print(f"[red]Hata: {e}[/red]")
            return None

    def Learn_TTL_Value(self,ip_address):
            icmp_packet = scapy.IP(dst=ip_address) / scapy.ICMP()
            answered, _ = scapy.sr(icmp_packet, timeout=2, verbose=0)

            if answered:
                for _, value in answered:
                    # print(f"[ ✔ ][snow] TTL Değeri:[/snow] {value.ttl}")
                    return value.ttl
            else:
                print("[red]Hedefe ulaşılamıyor[/]")
                return None

    def Os_Detection(self,ip_address):
            ttl_value = self.Learn_TTL_Value(ip_address)
            window_size_value = self.Learn_Window_Size_With_SYN_Packet(ip_address)

            if ttl_value is None or window_size_value is None:
                print("[red]İşletim sistemi tespit edilemedi.[/red]")
                return

            if 0 < ttl_value <= 64:
                if window_size_value in [29200, 8760, 14600, 5792, 65535]:
                    return "[green]OS: OpenBSD / Modern Linux Dist.[/green]"
                elif window_size_value == 5840:
                    return "[green]OS: Linux 2.4.x - 2.6.x[/green]"
                elif window_size_value in [16384, 32768]:
                    return "[green]OS: OpenBSD Or NetBSD[/green] "
                elif window_size_value == 65535:
                    return "[green]OS: FreeBSD veya macOS olabilir[/green]"
                else:
                    return "[yellow]OS: Unix/Linux Türevi (kesin değil)[/yellow]"

            elif 65 <= ttl_value <= 128:
                if window_size_value in [8192, 16384, 65535, 62240]:
                    return "[blue]🪟 OS: Windows[/blue]"
                else:
                    return "[yellow]OS: Muhtemelen Windows ama emin değiliz[/yellow]"

            elif 129 <= ttl_value <= 255:
                return "[cyan]OS: Cisco Router / Ağ Cihazı olabilir[/cyan]"

            else:
                return "[yellow]❓ OS: Bilinmeyen[/yellow]"

    def proxy_connect(self,option=None):
            try:
                if option == "random":
                    req = requests.get(
                        'https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all')
                    if req.status_code == 200:
                        print("Proxy adreslerine ulaşılıyor...")
                        proxy_list = req.text.splitlines()
                        selected_proxy = random.choice(proxy_list)
                        proxy_to_test = selected_proxy
                    else:
                        print("Proxy listesine erişilemedi.")
                        return None
                else:
                    proxy_to_test = option

                if proxy_to_test:
                    ip, port = proxy_to_test.split(":")
                    try:
                        print(f"Proxy test ediliyor: {ip}:{port}")
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
                            proxy_socket.settimeout(5)
                            proxy_socket.connect((ip, int(port)))
                            print("Proxy TCP bağlantısı başarılı.")

                        proxies = {
                            "http": f"http://{proxy_to_test}",
                            # "https": f"http://{proxy_to_test}",
                        }
                        test = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=5)
                        if test.status_code == 200:
                            print("Proxy HTTP isteğiyle de çalışıyor.")
                            return proxy_to_test
                        else:
                            print("Proxy HTTP üzerinden çalışmıyor.")
                            return None

                    except Exception as e:
                        print(f"Proxy bağlantı hatası: {e}")
                        return None
                else:
                    print("Proxy belirtilmedi.")
                    return None

            except Exception as e:
                print(f"Genel hata: {e}")
                return None

    def SiteCheck(self):
            try:
                Url = requests.get("https://api.macvendors.com/44:38:39:ff:ef:57", allow_redirects=True)
                if Url.status_code == 200:
                    print(f"{Url.status_code}")
                else:
                    print("I can't reach", Url.status_code)
            except Exception as e:
                print("Error:", e)

    def get_mac_vendor(self,mac_address: str) -> str:
            url = f"https://api.macvendors.com/{mac_address}"
            try:
                response = requests.get(url)
                sleep(1)
                response.raise_for_status()
                return response.text
            except requests.exceptions.RequestException:
                return "Error: Unknown Vendor"
            else:
                return "Error: Proxy not available"

    def generate_fake_ip(self,ip_class=None):

            if ip_class == 'A':

                return f"10.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
            elif ip_class == 'B':
                return f"172.{random.randint(16, 31)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
            elif ip_class == 'C':
                return f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}"
            else:
                # Tamamen rastgele (Public IP gibi görünür)
                return f"{random.randint(1, 223)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"

    def tcp_packet_with_scapy(self,target_ip, ip_class=None, count=1):
            # count=1 yaptık çünkü döngü zaten ana fonksiyonun içinde
            fake_src = self.generate_fake_ip(ip_class)
            src_port = random.randint(1024, 65535)
            dst_port = random.randint(1, 1024)
            packet = scapy.IP(src=fake_src, dst=target_ip) / scapy.TCP(sport=src_port, dport=dst_port, flags='S')
            scapy.send(packet, verbose=False)
            print(f"[bold cyan][+][/bold cyan] Sahte TCP Paketi: {fake_src} -> {target_ip}")

    def icmp_packet_with_scapy(self,ip_address, ip_class, data="This World Shall Know Pain"):
            src_ip = self.generate_fake_ip(ip_class)  # Burada ismi düzelttik
            packet = scapy.IP(dst=ip_address, src=src_ip) / scapy.ICMP() / data
            scapy.send(packet, verbose=False)
            print("icmp paketi oluşturuldu : ", src_ip, "->", ip_address)

    def send_spoofed_tcp(self,target_ip, ip_class=None, count=5):
            """Hedefe birden fazla sahte IP üzerinden SYN paketi gönderir."""
            for _ in range(count):
                fake_src = self.generate_fake_ip(ip_class)
                src_port = random.randint(1024, 65535)
                dst_port = random.randint(1, 1024)  # Genellikle servis portları

                # Paket oluşturma
                packet = scapy.IP(src=fake_src, dst=target_ip) / \
                         scapy.TCP(sport=src_port, dport=dst_port, flags='S')

                try:
                    scapy.send(packet, verbose=False)
                    print(f"[bold cyan][+][/bold cyan] Sahte Paket Gönderildi: {fake_src} -> {target_ip}")
                except Exception as e:
                    print(f"Hata: {e}")









    def PortScannerWithUDP(self,ip_address: str, port: int) -> bool:

            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
                client.sendto(b'', (ip_address, port))  # Boş bir UDP paketi gönder b''(boş byte anlamına gelir )
                client.settimeout(1)
                try:
                    data, _ = client.recvfrom(1024)  # 1024 bayt kadar veri al data,_ ilk bilgiyi al
                    return bool(data)
                except socket.error:
                    return False

    def PortScannerWithTCP(self,ip_address: str, port: int) -> bool:

            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                    client.settimeout(1)  # Bağlantı Zaman Aşımı Süresi
                    client.connect((ip_address, port))
                    return True
            except (socket.timeout, socket.error):
                return False

    def PortScannerWithSYN(self,ip_address: str, port: int) -> bool:
            try:
                # Tek bir SYN paketi gönderiyoruz
                response = scapy.sr1(scapy.IP(dst=ip_address) / scapy.TCP(dport=port, flags="S"), timeout=1, verbose=False)
                if response:
                    if response.haslayer(scapy.TCP):
                        # 0x12 -> SYN + ACK (Port Açık)
                        if response[scapy.TCP].flags == 0x12:
                            # Bağlantıyı düzgünce kapatmak için RST gönderiyoruz (Opsiyonel ama kibar bir tarama için)
                            scapy.send(scapy.IP(dst=ip_address) / scapy.TCP(dport=port, flags="R"), verbose=False)
                            return True
                        # 0x14 -> RST + ACK (Port Kapalı)
                        elif response[scapy.TCP].flags == 0x14:
                            return False
                return False
            except Exception as e:
                return False

    def PortScannerWithACK(self,ip_address: str, port: int) -> bool:
            response = scapy.sr1(scapy.IP(dst=ip_address) / scapy.TCP(dport=port, flags="A"), timeout=2, verbose=False)
            try:
                if response and response.haslayer(scapy.TCP):
                    tcp_flags = response[scapy.TCP].flags
                    # SYN + ACK bayrağı kontrolü
                    if tcp_flags == 0x12 or tcp_flags == "SA":  # SYN + ACK bayrakları bit maskesi
                        return True

                    elif tcp_flags == 0x02 or tcp_flags == "S":
                        return True

                    elif tcp_flags == 0x10 or tcp_flags == "A":
                        return True

                    elif tcp_flags & 0x14 or tcp_flags == "R":  # RST bayrağı bit maskesi
                        return False

            except Exception as e:
                print("Error : ", e)

    def PortScannerWithFIN(self,ip_address: str, port: int) -> bool:
            response = scapy.sr1(scapy.IP(dst=ip_address) / scapy.TCP(dport=port, flags="F"), verbose=False, timeout=2)
            try:
                if response and response.haslayer(scapy.TCP):
                    tcp_flags = response[scapy.TCP].flags
                    if tcp_flags == "A" or tcp_flags == 0x01:
                        return True

                    elif tcp_flags == 0x14 or tcp_flags == "R":
                        return False

                return False

            except Exception as e:
                print(f"[bold red ] Error [/bold red], {e} ")
                return False