#!/bin/bash
# run.sh - Simple wrapper to run the scanner

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "\033[1;34m[*] Running Network Vulnerability Scanner...\033[0m"
sudo python3 "$SCRIPT_DIR/scanner.py" "$@"
