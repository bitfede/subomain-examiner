###
# AUTHOR: Federico De Faveri
# DATE: July 2019
# PURPOSE: Python tool to perform recon on a list of subdomains
###

import argparse


parser = argparse.ArgumentParser()

# get arguments from command line
parser.add_argument("-i", help="pathname of the INPUT file")
parser.add_argument("-o", help="pathname of the OUTPUT file")

args = parser.parse_args()

inputfile = None
outputfile = None

inputfile = args.i
outputfile = args.o

if inputfile is None or outputfile is None:
    print("[!] No inputfile or outputfile flag specified")
    print("[i] Usage: subdomain-examiner -i path/to/inputfile -o path/to/outputfile")
    print("[!] Exiting")
    exit(1)


print(f"input: {inputfile} | output: {outputfile}")
