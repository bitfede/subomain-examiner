#! /usr/bin/env python3

import socket
import nmap

nm = nmap.PortScanner()

def examine(subdomain_data):

    ip_addr = socket.gethostbyname(subdomain_data)

    print(f"[*] Examining {subdomain_data} | IP: {ip_addr}")

    nm.scan(subdomain_data, arguments='-sS -Pn -p-')

    print(nm.all_hosts())

    results = {}
    results["Hostname"] = nm[ip_addr].hostname()
    results["State"] = nm[ip_addr].state()
    results["Ports"] = []

    for key in nm[ip_addr]['tcp'].keys():
        # print(nm[ip_addr]['tcp'][key])
        port_data = {
            "portNumber": key,
            "PortStatus": nm[ip_addr]['tcp'][key]
        }

        results["Ports"].append(port_data)


    # print(results)

    return results
