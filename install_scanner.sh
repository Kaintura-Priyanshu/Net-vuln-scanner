#!/bin/bash
# install_scanner.sh

echo "[*] Installing Network Vulnerability Scanner dependencies..."

# Update package list
sudo apt update

# Install Python dependencies
pip3 install -r requirements.txt

# Install additional Kali Linux tools
sudo apt install -y nmap

sudo apt install -y metasploit-framework

sudo apt install -y exploitdb

echo "[+] Installation complete!"
