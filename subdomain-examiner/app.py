###
# AUTHOR: Federico De Faveri
# DATE: July 2019
# PURPOSE: Python tool to perform recon on a list of subdomains
###

from examiner import examine
import argparse
import os

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

#for each subdomain call the scanner method/s
for subdomain in subdomains:
    scan_res = examine(subdomain)
    examined_hostname = scan_res["Hostname"]
    print("[>] Scan Results for", examined_hostname)
    for port in scan_res["Ports"]:
        port_number = port['portNumber']
        port_status = port['portStatus']['state']
        port_name = port['portStatus']['name']
        print(f"[*] Port {port_number} is {port_status} | Service: {port_name}")
        repfilename = f"{port_number}_{port_name}.txt"

        reportfile = open(repfilename, 'a')
        reportfile.write(f"{examined_hostname}\n")


#exit gracefully
exit(0)
