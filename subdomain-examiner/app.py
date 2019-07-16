#! /usr/bin/env python3

###
# AUTHOR: Federico De Faveri
# DATE: July 2019
# PURPOSE: Python tool to perform recon on a list of subdomains
###

import argparse
import os

parser = argparse.ArgumentParser()

# get arguments from command line
parser.add_argument("-i", help="pathname of the INPUT file, a list of subdomains")

args = parser.parse_args()

inputfile = None

inputfile = args.i

if inputfile is None:
    print("[!] No inputfile or outputfile flag specified")
    print("[i] Usage: subdomain-examiner -i path/to/inputfile")
    print("[!] Exiting")
    exit(1)
else:
    print(f"[*] Reading subdomains from: {inputfile}")

# check if they are valid files
is_inputfile_valid = os.path.isfile(inputfile)

print(f"1 {is_inputfile_valid}")

# parse the file and get an array of subdomains

#for each subdomain call the scanner method/s

#get back structured results and call reporting method/s

#exit gracefully
exit(0)
