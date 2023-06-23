import nmap
from tabulate import tabulate

def scan_ports(ip):
    open_ports = []
    
    nm = nmap.PortScanner()
    nm.scan(ip, arguments='-p1-65535 -sV --open')
    
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                protocol = proto
                service = nm[host][proto][port]['name']
                version = nm[host][proto][port]['version']
                open_ports.append((port, protocol, service, version))
    
    return open_ports

# Punto de entrada del script
ip = input("\033[34mIngresa la dirección IP que deseas escanear:\033[34m")
open_ports = scan_ports(ip)

table = [["Port", "Protocol", "Service", "Version"]]
table.extend(open_ports)

purple_banner = """
\033[95m

          ##  ##              ####     ##     ##   ##
   V.0.8  ##  ##             ##  ##   ####    ###  ##
 ######   ##  ##    #####   ##       ##  ##   #### ##
  ##  ##   ####    ##       ##       ##  ##   ## ####
  ##  ##    ##      #####   ##       ######   ##  ###
  #####     ##          ##   ##  ##  ##  ##   ##   ##
  ##       ####    ######     ####   ##  ##   ##   ## 
 ####                        By: killerpop(G.Zaballa)
                                     
\033[0m"""

print(purple_banner)
print(tabulate(table, headers="firstrow", tablefmt="grid"))