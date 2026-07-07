#!/usr/bin/env python3
"""
Network Vulnerability Scanner Wrapper
Alternative way to run the scanner
"""

import sys
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    scanner_path = os.path.join(script_dir, 'scanner.py')
    
    if not os.path.exists(scanner_path):
        print(f"[-] Error: scanner.py not found")
        sys.exit(1)
    
    # Execute the scanner with arguments
    sys.argv = [scanner_path] + sys.argv[1:]
    
    with open(scanner_path, 'r') as f:
        code = f.read()
        exec(compile(code, scanner_path, 'exec'), {'__name__': '__main__', '__file__': scanner_path})

if __name__ == "__main__":
    main()
