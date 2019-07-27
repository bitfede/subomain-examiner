#! /usr/bin/env python3

import socket
import nmap

nm = nmap.PortScanner()

def examine(subdomain_data):

    try:
        ip_addr = socket.gethostbyname(subdomain_data)
    except socket.error:
        return {}

    print(f"[*] Examining {subdomain_data} | IP: {ip_addr}")

    nm.scan(subdomain_data, arguments='-sS -Pn')

    results = {}
    results["Hostname"] = nm[ip_addr].hostname()
    results["State"] = nm[ip_addr].state()
    results["Ports"] = []

    print(nm.all_hosts())
    print('--------')
    print(nm[ip_addr])
    print('--------')

    if 'tcp' not in nm[ip_addr]:
        return results

    for key in nm[ip_addr]['tcp'].keys():
        # print(nm[ip_addr]['tcp'][key])
        port_data = {
            "portNumber": key,
            "portStatus": nm[ip_addr]['tcp'][key]
        }

        results["Ports"].append(port_data)


    # print(results)

    return results
