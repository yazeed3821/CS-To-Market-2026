# TCP Network Port Scanner

A lightweight network reconnaissance tool engineered in Python to identify open TCP ports and active services across target machines.

## Overview
During the reconnaissance phase of a security assessment, mapping exposed attack surfaces is critical. This utility implements non-blocking TCP socket connections to audit listening services within specified IP addresses.

## Architecture & Features
* **Socket Handshakes:** Utilizes standard `AF_INET` and `SOCK_STREAM` protocols.
* **Timeout Governance:** Configured connection timeouts (1s) to balance scan speed and packet loss prevention.
* **Standard Target Scope:** Pre-configured for common vector ports (FTP: 21, SSH: 22, HTTP: 80, HTTPS: 443, MySQL: 3306).

## Usage

```bash
python port_scanner.py

```
## Sample output
Starting scan on target: 127.0.0.1
[+] Port 80 is OPEN on 127.0.0.1
Scan completed in 1.05 seconds