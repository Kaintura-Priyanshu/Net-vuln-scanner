#!/usr/bin/env python3
"""
This wrapper fixes the 'import * only allowed at module level' issue
without modifying the original scanner.py
"""

import sys
import os
import importlib.util
import argparse

def main():
    """Run the scanner with proper imports"""
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    scanner_path = os.path.join(script_dir, 'scanner.py')
    
    # Check if scanner.py exists
    if not os.path.exists(scanner_path):
        print(f"[-] Error: scanner.py not found in {script_dir}")
        sys.exit(1)
    
    # Add the script directory to Python path
    sys.path.insert(0, script_dir)
    
    try:
        # Import the scanner module dynamically
        spec = importlib.util.spec_from_file_location("scanner", scanner_path)
        scanner_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(scanner_module)
        
        # Preserve command line arguments
        sys.argv = ['scanner.py'] + sys.argv[1:]
        
        # Run the main function
        scanner_module.main()
        
    except ImportError as e:
        print(f"[-] Import error: {e}")
        print("[!] Make sure all dependencies are installed")
        print("[!] Run: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
