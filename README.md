# Network Vulnerability Scanner

A comprehensive network vulnerability scanner designed for Kali Linux environment setups to perform automated port scanning, service detection, and vulnerability identification.

---

## Features

* **Port Scanning:** Fast, multi-threaded TCP port scanning.
* **Service Detection:** Banner grabbing and service fingerprinting capabilities.
* **Vulnerability Tracking:** Identifies known version mismatches and common risks.
* **Web Directory Assessment:** Basic directory listing checks and default page exposure detection.
* **Network Reconnaissance:** Local DNS resolution and host status discovery.
* **Detailed Reporting:** Generates structured JSON data and color-coded terminal alerts.
* **Nmap Integration:** Leverages the robust `python-nmap` abstraction layer.

---

## Prerequisites

* **Operating System:** Kali Linux (Recommended) or any Debian-based Linux distribution.
* **Python Version:** Python 3.6+
* **Privileges:** Root/Administrator access (required for raw socket operations and deeper Nmap scanning).

### Required Python Packages

```bash
colorama==0.4.6      # Colored terminal output
python-nmap==0.7.1   # Nmap engine abstraction
requests==2.31.0     # HTTP assessment interaction
scapy==2.5.0         # Network packet manipulation
```

### Installation

## Method 1: Automated Installation (Recommended)

# Clone the repository
git clone https://github.com/Kaintura-Priyanshu/Net-vuln-scanner.git

cd network-vulnerability-scanner

# Make installation script executable
chmod +x install_scanner.sh

# Run installation
sudo ./install_scanner.sh

## Method 2: Manual Installation

# Install Python dependencies
pip3 install -r requirements.txt

# Install additional Kali tools
sudo apt update
sudo apt install -y nmap
sudo apt install -y metasploit-framework
sudo apt install -y exploitdb

# Make scanner executable
chmod +x scanner.py

# Usage

Basic Usage

# Scan a single host
sudo python3 scanner.py 192.168.1.100

# Scan with custom ports
sudo python3 scanner.py 192.168.1.100 -p 1-1000

# Scan with verbose output
sudo python3 scanner.py example.com -v

# Command Line Options

Option	Description	Example

target	Target IP address or hostname (required)	192.168.1.1

-p, --ports	Port range to scan	-p 1-1000

-v, --verbose	Verbose output	-v

-h, --help	Show help message	-h

# Examples

# Scan local network
sudo python3 scanner.py 192.168.1.1

# Scan specific ports
sudo python3 scanner.py 10.0.0.1 -p 22,80,443,3306

# Scan with verbose output
sudo python3 scanner.py scanme.nmap.org -v

# Full scan with all options
sudo python3 scanner.py 192.168.1.100 -p 1-65535 -v

## Scan Capabilities

### Detected Vulnerabilities

| Category | Vulnerabilities | Severity |
| :--- | :--- | :--- |
| **FTP** | vsftpd 2.3.4 (Backdoor), ProFTPD 1.3.3c (RCE) | 🔴 High |
| **Web** | Apache 2.2.8, nginx 1.0.15, IIS 6.0 | 🟠 Medium |
| **SSL/TLS** | OpenSSL 1.0.1 (Heartbleed), OpenSSL 1.0.2a | 🔴 High |
| **SSH** | OpenSSH 4.7, OpenSSH 5.1 | 🔴 High |
| **MySQL** | MySQL 5.0, MySQL 5.1 | 🟠 Medium |
| **SMB** | EternalBlue (MS17-010) | 🔴 High |
| **Web** | Directory Listing Enabled | 🟠 Medium |
| **Web** | Default Pages Exposed | 🟡 Low |

### Ports Scanned by Default

| Port | Service | Port | Service |
| :--- | :--- | :--- | :--- |
| **21** | FTP | **443** | HTTPS |
| **22** | SSH | **445** | SMB |
| **23** | Telnet | **993** | IMAPS |
| **25** | SMTP | **995** | POP3S |
| **53** | DNS | **1723** | PPTP |
| **80** | HTTP | **3306** | MySQL |
| **110** | POP3 | **3389** | RDP |
| **111** | RPCbind | **5432** | PostgreSQL |
| **135** | MSRPC | **5900** | VNC |
| **139** | NetBIOS | **6379** | Redis |
| **143** | IMAP | **27017** | MongoDB |

# Output & Reports

The scanner provides color-coded output for easy reading:

🟢 Green - Open ports and success messages

🔴 Red - Vulnerabilities detected

🟡 Yellow - Warnings and information

🔵 Cyan - Progress updates

## Scanner Banner

```bash
╔══════════════════════════════════════════════════════════╗
║     Network Vulnerability Scanner v1.0                  ║
║     Kali Linux Security Tool                            ║
╚══════════════════════════════════════════════════════════╝
Target: 192.168.1.100
Time: 2026-01-06 14:30:22
============================================================
```

## Scan in Progress
text
[*] Performing network reconnaissance...
[+] Hostname: target-host.local

[*] Starting port scan on 192.168.1.100...
[+] Port 21 (FTP) is open
[+] Port 22 (SSH) is open
[+] Port 80 (HTTP) is open
[!] VULNERABILITY DETECTED on port 21: vsftpd 2.3.4
[!] VULNERABILITY DETECTED on port 80: Apache/2.2.8

##Scan Report

```bash
============================================================
SCAN REPORT
============================================================
Target: 192.168.1.100
Scan Time: 2026-01-06 14:30:22
Operating System: Linux 2.6.32
Hostname: target-host.local

Open Ports: 3
  [21] FTP - vsftpd 2.3.4
  [22] SSH - OpenSSH 4.7
  [80] HTTP - Apache/2.2.8

Vulnerabilities Found: 2
  [!] Port 21: Potential vulnerability: vsftpd 2.3.4
      Severity: High
      Recommendation: Update to latest version
  [!] Port 80: Potential vulnerability: Apache/2.2.8
      Severity: High
      Recommendation: Update to latest version

[+] Report saved to: scan_report_192.168.1.100_20260106_143022.json

```
### Development Setup

# Clone your fork
git clone https://github.com/Kaintura-Priyanshu/Net-vuln-scanner.git

# Install development dependencies
pip3 install -r requirements.txt

# Run tests
python3 -m pytest tests/

# Disclaimer
IMPORTANT: This tool is intended for educational purposes and authorized security testing only.

 Use only on systems you own or have permission to test

 Follow all applicable laws and regulations

 Report vulnerabilities responsibly

 Do NOT use for malicious purposes

 Do NOT scan systems without explicit permission

The authors are not responsible for any misuse or damage caused by this tool. By using this tool, you agree to take full responsibility for your actions.


## MIT License

Copyright (c) 2026 Security Scanner Tool

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Future Plans

Add CVE database integration

Implement exploit suggestions

Add SQL injection detection

Add XSS vulnerability scanning

Implement automated remediation suggestions

Add HTML/PDF report generation



"If you know the enemy and know yourself, you need not fear the result of a hundred battles."

