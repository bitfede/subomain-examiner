# Subdomain Examiner

## What is it?

A simple recon tool that allows you to scan a whole list of subdomains and identify which of these servers have open services.

Requires superuser permission to run because it uses the nmap SYN scan. Make sure you review and acknowledge the code before running it on your system.

## How do I install it?

TODO

## How do I use it?

Command usage:
```
sudo subdomain-examiner -i subdomains.txt
```

The argument `subdomains.txt` has one subdomain per line:
```
subdomain1.example.com
subdomain2.example.com
subdomain3.example.com
subdomain4.example.com
```

The examiner will start scanning

## DISCLAIMER

Do NOT use this software for malicious purposes, I am not responsible for whatever damage you cause.

Make sure you have explicit permission from the subdomains owner before testing them.
