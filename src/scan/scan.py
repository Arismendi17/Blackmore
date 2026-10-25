from colorama import Fore, Style
import nmap

scanner = nmap.PortScanner()


def scan_hosts(hosts):
    print(Fore.GREEN + "Scanning...\n" + Style.RESET_ALL)
    scanner.scan(hosts)


scan_hosts("192.168.0.1/24")

print(Fore.BLUE + "Hosts found:" + Style.RESET_ALL)
for host in scanner.all_hosts():
    print(host)
print()
