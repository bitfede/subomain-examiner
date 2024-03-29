#!/usr/bin/env python3

###
# AUTHOR: Federico De Faveri
# DATE: July 2019
# PURPOSE: Python tool to perform recon on a list of subdomains
###

from examiner import examine
import argparse
import os
import time

parser = argparse.ArgumentParser()

# get arguments from command line
parser.add_argument("-i", help="pathname of the INPUT file, a list of subdomains")

args = parser.parse_args()

inputfile = None

inputfile = args.i

if inputfile is None:
    print("[!] No inputfile flag specified")
    print("[!] Exiting")
    print("[i] Usage: subdomain-examiner -i path/to/inputfile")
    exit(1)
else:
    print(f"[*] Reading subdomains from: {inputfile}")

# check if they are valid files
is_inputfile_valid = os.path.isfile(inputfile)

if is_inputfile_valid is False:
    print("[!] The inputfile is not a valid file path")
    print("[!] Exiting")
    exit(2)

# parse the file and get an array of subdomains
inputfile = open(inputfile, 'r')

subdomains = inputfile.read().split('\n')
subdomains.pop()
inputfile.close()

scanner_results_arr = []

# creates folder to store results into
localtime = time.asctime( time.localtime(time.time()) )
dirname  = "scan-" + localtime.replace(" ", "-").replace(":", "-")
os.mkdir(dirname)

# for each subdomain call the scanner method/s
for subdomain in subdomains:
    scan_res = examine(subdomain)
    if scan_res == {}:
        continue
    if len(scan_res['Ports']) == 0:
        continue

    examined_hostname = scan_res["Hostname"]
    print("[>] Scan Results for", examined_hostname)
    for port in scan_res["Ports"]:
        port_number = port['portNumber']
        port_status = port['portStatus']['state']
        port_name = port['portStatus']['name']
        print(f"[*] Port {port_number} is {port_status} | Service: {port_name}")
        repfilename = f"{port_number}_{port_name}.txt"

        reportfile = open(f"{dirname}/{repfilename}", 'a')
        reportfile.write(f"{examined_hostname}\n")
#get back structured results and call reporting method/s
# TODO create files for each open port type and name them {port_number}-{port_name}

#exit gracefully
exit(0)
