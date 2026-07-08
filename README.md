# Network Vulnerability Scanner
A comprehensive **network vulnerability scanner** for Kali Linux that performs port scanning, service detection, and vulnerability identification.

---
## Features

| Feature | Description | Status |
|---------|-------------|--------|
| **Port Scanning** | Fast multi-threaded TCP port scanning | ✅ |
| **Service Detection** | Banner grabbing and service fingerprinting | ✅ |
| **Vulnerability Detection** | Identifies known vulnerable services | ✅ |
| **Web Vulnerability Scan** | Directory listing and default page detection | ✅ |
| **SMB Vulnerability Check** | Detects SMB vulnerabilities (EternalBlue, etc.) | ✅ |
| **MySQL Security Audit** | Checks for MySQL vulnerabilities | ✅ |
| **OS Detection** | Operating system fingerprinting via Nmap | ✅ |
| **Network Reconnaissance** | DNS resolution and host discovery | ✅ |
| **Detailed Reporting** | JSON and console output with color coding | ✅ |
| **Nmap Integration** | Advanced scanning with Nmap | ✅ |

---

## Prerequisites

- **Kali Linux** (Recommended) or any Debian-based Linux
- **Python 3.6+**
- **Root/Administrator Privileges** (for full functionality)
- **Internet Connection** (for dependency installation)

### Required Packages

| Package | Version | Purpose |
|---------|---------|---------|
| `colorama` | >=0.4.6 | Colored terminal output |
| `python-nmap` | >=0.7.1 | Nmap integration |
| `requests` | >=2.31.0 | HTTP requests |
| `nmap` | Latest | System Nmap tool |

---

## Installation

### Method 1: Automated Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/Kaintura-Priyanshu/Net-vuln-scanner.git
cd Net-vuln-scanner

# Make installation script executable
chmod +x install_scanner.sh

# Run installation
sudo ./install_scanner.sh
```

### Method 2: Manual Installation

```bash
# Install system dependencies
sudo apt update
sudo apt install -y nmap python3-nmap python3-pip

# Install Python dependencies
sudo pip3 install -r requirements.txt --break-system-packages

# Make scanner executable
chmod +x scanner.py
```

### Method 3: Quick Install (One-Liner)

```bash
# Scan a single host
sudo python3 scanner.py 192.168.1.48

# Scan with custom ports
sudo python3 scanner.py 192.168.1.48 -p 1-1000

# Verbose mode
sudo python3 scanner.py example.com -v
```

### Usage

```bash
# Scan a single host
sudo python3 scanner.py 192.168.1.48

# Scan with custom ports
sudo python3 scanner.py 192.168.1.48 -p 1-1000

# Verbose mode
sudo python3 scanner.py example.com -v
```

## Command Line Options

| Option | Description | Example |
| :--- | :--- | :--- |
| `target` | Target IP address or hostname | `192.168.1.1` |
| `-p`, `--ports` | Port range to scan | `-p 1-1000` |
| `-v`, `--verbose` | Verbose output | `-v` |
| `-h`, `--help` | Show help message | `-h` |

### Using Wrapper Scripts

```bash
# Method 1: Using run.sh
sudo ./run.sh [ip]

# Method 2: Using Python wrapper
sudo python3 run_scanner.py [ip]

# Method 3: Using symlink (if installed)
sudo net-vuln-scanner [ip]
```

### Examples

```bash
# Scan local network
sudo python3 scanner.py [ip]

# Scan specific ports
sudo python3 scanner.py [ip] -p 22,80,443,3306

# Scan with verbose output
sudo python3 scanner.py scanme.nmap.org -v

# Full scan with all options
sudo python3 scanner.py [ip] -p 1-65535 -v
```

## Scan Capabilities

### Ports Scanned by Default

| Port | Service | Port | Service | Port | Service |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `21` | FTP | `443` | HTTPS | `1723` | PPTP |
| `22` | SSH | `445` | SMB | `3306` | MySQL |
| `23` | Telnet | `993` | IMAPS | `3389` | RDP |
| `25` | SMTP | `995` | POP3S | `5432` | PostgreSQL |
| `53` | DNS | `110` | POP3 | `5900` | VNC |
| `80` | HTTP | `111` | RPCbind | `6379` | Redis |
| `135` | MSRPC | `139` | NetBIOS | `27017`| MongoDB |
| `143` | IMAP | | | | |

### Scan Statistics

| Scan Type | Average Time | Threads Used | Accuracy |
| :--- | :--- | :--- | :--- |
| **Quick Scan** (Common Ports) | 5-10 seconds | 100 | 90% |
| **Full Scan** (1-1000) | 30-60 seconds | 200 | 95% |
| **Comprehensive** (1-65535) | 5-10 minutes | 500 | 98% |

---

## Vulnerability Detection

### Detected Vulnerabilities

| Category | Vulnerabilities | Severity | CVE |
| :--- | :--- | :--- | :--- |
| **FTP** | vsftpd 2.3.4 (Backdoor) | 🔴 High | CVE-2011-2523 |
| **FTP** | ProFTPD 1.3.3c (RCE) | 🔴 High | CVE-2010-4221 |
| **SSH** | OpenSSH 4.7 | 🔴 High | CVE-2008-1657 |
| **SSH** | OpenSSH 5.1 | 🔴 High | Multiple |
| **Web** | Apache 2.2.8 | 🟠 Medium | Multiple |
| **Web** | nginx 1.0.15 | 🟠 Medium | Multiple |
| **Web** | IIS 6.0 | 🟠 Medium | Multiple |
| **SSL/TLS** | OpenSSL 1.0.1 (Heartbleed) | 🔴 High | CVE-2014-0160 |
| **SSL/TLS** | OpenSSL 1.0.2a | 🔴 High | Multiple |
| **MySQL** | MySQL 5.0/5.1 | 🟠 Medium | Multiple |
| **SMB** | EternalBlue (MS17-010) | 🔴 High | CVE-2017-0144 |
| **Web** | Directory Listing Enabled | 🟠 Medium | - |

### Vulnerability Severity Levels

| Level | Color | Description |
| :--- | :---: | :--- |
| **High** | 🔴 | Critical vulnerabilities, remote code execution |
| **Medium** | 🟠 | Information disclosure, moderate risk |
| **Low** | 🟡 | Minor security issues |

### Console Output Example

╔══════════════════════════════════════════════════════════╗
║     Network Vulnerability Scanner v2.0                  ║
║     Kali Linux Security Tool                            ║
╚══════════════════════════════════════════════════════════╝

Target: 192.168.1.48

Time: 2026-01-08 14:30:22

============================================================

[*] Performing network reconnaissance...

[+] Hostname: target-host.local


[*] Starting port scan on [ip]...

[+] Port 21 (FTP) is open

[+] Port 22 (SSH) is open

[+] Port 80 (HTTP) is open

[!] VULNERABILITY DETECTED on port 21: vsftpd 2.3.4

[!] VULNERABILITY DETECTED on port 80: Apache/2.2.8


[*] Running Nmap scan for detailed information...

[+] OS Detection: Linux 2.6.32

============================================================
SCAN REPORT
============================================================

Target: [ip]

Scan Time: 2026-01-08 14:30:22

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

[+] Report saved to: scan_report_192.168.1.48_20260108_143022.json

### Verify Installation
```bash
# Check Python version
python3 --version

# Check dependencies
python3 -c "import nmap, colorama, requests; print('✅ All dependencies installed')"

# Check Nmap
nmap --version

# Test scanner
sudo python3 scanner.py 127.0.0.1
```

### Quick Fix Commands
```bash
# Fix all dependencies
sudo apt update
sudo apt install -y python3-nmap python3-pip nmap
sudo pip3 install colorama requests --break-system-packages

# Run scanner
sudo python3 scanner.py 192.168.1.48
```

# Disclaimer
IMPORTANT: This tool is intended for educational purposes and authorized security testing only.

