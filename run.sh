#!/bin/bash
# run.sh - Bash wrapper for Network Vulnerability Scanner
# This wrapper runs scanner.py without modifying the original file

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCANNER_PATH="$SCRIPT_DIR/scanner.py"

# Check if scanner.py exists
if [ ! -f "$SCANNER_PATH" ]; then
    echo "[-] Error: scanner.py not found in $SCRIPT_DIR"
    exit 1
fi

# Run the scanner using Python's exec
sudo python3 -c "
import sys
import os
sys.path.insert(0, '$SCRIPT_DIR')
exec(open('$SCANNER_PATH').read())
" "$@"
