#!/bin/bash
# install_scanner.sh - Complete installation script for Network Vulnerability Scanner

echo -e "\033[1;34m[*] Installing Network Vulnerability Scanner...\033[0m"

# Check for root privileges
if [ "$EUID" -ne 0 ]; then 
    echo -e "\033[1;31m[-] Please run as root: sudo $0\033[0m"
    exit 1
fi

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "\033[1;34m[*] Updating package list...\033[0m"
apt update -qq

echo -e "\033[1;34m[*] Installing system dependencies...\033[0m"
apt install -y nmap python3-pip

echo -e "\033[1;34m[*] Installing Python dependencies...\033[0m"
pip3 install --upgrade pip -q
pip3 install -r requirements.txt -q

echo -e "\033[1;34m[*] Making scripts executable...\033[0m"
chmod +x scanner.py
chmod +x run.sh

echo -e "\033[1;34m[*] Creating symlink for easy access...\033[0m"
ln -sf "$SCRIPT_DIR/scanner.py" /usr/local/bin/net-vuln-scanner

echo -e "\033[1;32m[+] Installation complete!\033[0m"
echo ""
echo -e "\033[1;33m[*] Usage:\033[0m"
echo "  sudo net-vuln-scanner 192.168.1.48"
echo "  sudo python3 scanner.py 192.168.1.48"
echo "  sudo ./run.sh 192.168.1.48"
