from colorama import Fore, Style
import nmap


targets = "192.168.0.1/24"


# basic scan looking for up hosts
def scan_hosts(hosts):
    scanner = nmap.PortScanner()
    scanner.scan(
        hosts=targets,
        arguments="-sn"
    )
    return scanner


def scan_ports(scanner):
    results = {}
    # scan found hosts for selected ports
    for ip in list(scanner.all_hosts()):
        scanner.scan(
            hosts=ip,
            ports="22,53,80,443,554,8000,8080,8443",
            arguments="-sV --version-light"
        )

        host = scanner[ip]
        ports = []
        for protocol in host.all_protocols():
            for port in host[protocol]:
                info = host[protocol][port]
                ports.append({
                    "port": port,
                    "protocol": protocol,
                    "state": info.get("state"),
                    "service": info.get("name"),
                    "product": info.get("product"),
                    "version": info.get("version"),
                    "extrainfo": info.get("extrainfo"),
                })
        results[ip] = {
            "hostname": host.hostname() or "unknown",
            "state": host.state(),
            "ports": ports,
        }
    return results


def output_formatted(results):
    for ip, host in results.items():
        print(f"\n{ip} ({host['hostname']}) — {host['state']}")

        if not host["ports"]:
            print("  No selected ports found.")
            continue

        for item in host["ports"]:
            details = " ".join(
                part for part in (
                    item["product"],
                    item["version"],
                    item["extrainfo"],
                )
                if part
            )
            service = item["service"]
            if details:
                service += f" ({details})"

            print(
                f"  {item['protocol'].upper():<4} "
                f"{item['port']:<5} "
                f"{item['state']:<8} "
                f"{service}"
            )


print(Fore.GREEN + "Looking for hosts...\n" + Style.RESET_ALL)
found_hosts = scan_hosts(targets)

print(Fore.BLUE + "Hosts found, getting info...\n" + Style.RESET_ALL)
scan_results = scan_ports(found_hosts)
output_formatted(scan_results)
