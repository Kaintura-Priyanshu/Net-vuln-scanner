#!/usr/bin/env python3
import socket
import sys
import threading
import time
import json
import os
from datetime import datetime
from colorama import init, Fore, Style
import argparse

# Initialize colorama for colored output
init(autoreset=True)

class NetworkVulnerabilityScanner:
    def __init__(self, target):
        self.target = target
        self.results = {
            'target': target,
            'scan_time': datetime.now().isoformat(),
            'open_ports': [],
            'services': {},
            'vulnerabilities': [],
            'os_info': None,
            'network_info': None
        }
        self.common_ports = {
            21: 'FTP',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            80: 'HTTP',
            110: 'POP3',
            111: 'RPCbind',
            135: 'MSRPC',
            139: 'NetBIOS',
            143: 'IMAP',
            443: 'HTTPS',
            445: 'SMB',
            993: 'IMAPS',
            995: 'POP3S',
            1723: 'PPTP',
            3306: 'MySQL',
            3389: 'RDP',
            5432: 'PostgreSQL',
            5900: 'VNC',
            6379: 'Redis',
            27017: 'MongoDB'
        }
        
        # Vulnerability signatures
        self.vulnerability_signatures = {
            '21': ['vsftpd 2.3.4', 'proftpd 1.3.3c'],
            '80': ['Apache/2.2.8', 'nginx/1.0.15', 'IIS/6.0'],
            '443': ['OpenSSL/1.0.1', 'OpenSSL/1.0.2a'],
            '3306': ['MySQL 5.0', 'MySQL 5.1'],
            '22': ['OpenSSH 4.7', 'OpenSSH 5.1']
        }

    def banner(self):
        """Display tool banner"""
        banner_text = f"""
{Fore.GREEN}╔══════════════════════════════════════════════════════════╗
{Fore.GREEN}║     {Fore.YELLOW}Network Vulnerability Scanner v2.0{Fore.GREEN}          ║
{Fore.GREEN}║     {Fore.CYAN}Kali Linux Security Tool{Fore.GREEN}                     ║
{Fore.GREEN}╚══════════════════════════════════════════════════════════╝
{Fore.WHITE}Target: {Fore.YELLOW}{self.target}
{Fore.WHITE}Time: {Fore.YELLOW}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{Fore.WHITE}{'='*60}
        """
        print(banner_text)

    def port_scan(self, ports_range=None):
        """Perform TCP port scanning"""
        print(f"{Fore.CYAN}[*] Starting port scan on {self.target}...")
        
        if ports_range is None:
            ports_range = list(self.common_ports.keys())
        
        open_ports = []
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))
                if result == 0:
                    service = self.common_ports.get(port, 'Unknown')
                    open_ports.append(port)
                    print(f"{Fore.GREEN}[+] Port {port} ({service}) is open")
                    # Get service banner
                    try:
                        banner = self.get_banner(self.target, port)
                        if banner:
                            self.results['services'][port] = {
                                'service': service,
                                'banner': banner[:100]
                            }
                            self.check_vulnerability(port, banner)
                    except:
                        pass
                sock.close()
            except Exception:
                pass
        
        # Create threads for scanning
        threads = []
        for port in ports_range:
            thread = threading.Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()
            
            # Limit concurrent threads
            if len(threads) >= 100:
                for t in threads:
                    t.join()
                threads = []
        
        # Wait for remaining threads
        for t in threads:
            t.join()
        
        self.results['open_ports'] = open_ports
        print(f"{Fore.CYAN}[*] Port scan complete. Found {len(open_ports)} open ports.")
        return open_ports

    def get_banner(self, host, port, timeout=5):
        """Get service banner from port"""
        try:
            # Check if requests is available for HTTP
            if port in [80, 443, 8080, 8443]:
                try:
                    import requests
                    protocol = 'https' if port in [443, 8443] else 'http'
                    response = requests.get(f'{protocol}://{host}:{port}', timeout=timeout, verify=False)
                    server_header = response.headers.get('Server', '')
                    if server_header:
                        return f"HTTP Server: {server_header}"
                except:
                    pass
                return None
            else:
                # Other TCP services
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)
                sock.connect((host, port))
                
                # Send a probe
                if port == 22:  # SSH
                    sock.send(b"SSH-2.0-OpenSSH_Test\r\n")
                elif port == 21:  # FTP
                    sock.send(b"QUIT\r\n")
                elif port == 25:  # SMTP
                    sock.send(b"EHLO test\r\n")
                elif port == 110:  # POP3
                    sock.send(b"QUIT\r\n")
                
                banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                sock.close()
                return banner if banner else None
        except:
            return None

    def check_vulnerability(self, port, banner):
        """Check for known vulnerabilities based on service banner"""
        port_str = str(port)
        if port_str in self.vulnerability_signatures:
            for signature in self.vulnerability_signatures[port_str]:
                if signature.lower() in banner.lower():
                    vulnerability = {
                        'port': port,
                        'service': self.common_ports.get(port, 'Unknown'),
                        'vulnerability': f'Potential vulnerability: {signature}',
                        'severity': 'High',
                        'recommendation': 'Update to latest version'
                    }
                    self.results['vulnerabilities'].append(vulnerability)
                    print(f"{Fore.RED}[!] VULNERABILITY DETECTED on port {port}: {signature}")

    def advanced_vulnerability_scan(self):
        """Perform advanced vulnerability scanning using external tools"""
        print(f"{Fore.CYAN}[*] Starting advanced vulnerability scan...")
        
        # Check for common vulnerabilities
        if 80 in self.results['open_ports'] or 443 in self.results['open_ports']:
            self.check_web_vulnerabilities()
        
        if 445 in self.results['open_ports'] or 139 in self.results['open_ports']:
            self.check_smb_vulnerabilities()
        
        if 3306 in self.results['open_ports']:
            self.check_mysql_vulnerabilities()
        
        # Use nmap for detailed scan
        self.nmap_scan()

    def check_web_vulnerabilities(self):
        """Check for web vulnerabilities"""
        print(f"{Fore.YELLOW}[*] Checking web vulnerabilities...")
        
        try:
            import requests
            # Check for common web vulnerabilities
            for port in [80, 443, 8080, 8443]:
                if port in self.results['open_ports']:
                    protocol = 'https' if port in [443, 8443] else 'http'
                    url = f'{protocol}://{self.target}:{port}'
                    
                    try:
                        # Check for directory listing
                        response = requests.get(f'{url}/', timeout=5, verify=False)
                        if 'Index of /' in response.text:
                            vuln = {
                                'port': port,
                                'service': self.common_ports.get(port, 'Unknown'),
                                'vulnerability': 'Directory listing enabled',
                                'severity': 'Medium',
                                'recommendation': 'Disable directory listing'
                            }
                            self.results['vulnerabilities'].append(vuln)
                            print(f"{Fore.RED}[!] Directory listing enabled on {url}")
                        
                        # Check for default pages
                        default_pages = ['/default.asp', '/default.aspx', '/index.html', '/index.php']
                        for page in default_pages:
                            try:
                                resp = requests.get(f'{url}{page}', timeout=3, verify=False)
                                if resp.status_code == 200:
                                    print(f"{Fore.YELLOW}[*] Found page: {page}")
                            except:
                                pass
                                
                    except Exception:
                        pass
        except ImportError:
            print(f"{Fore.YELLOW}[!] Requests module not installed. Skipping web checks.")

    def check_smb_vulnerabilities(self):
        """Check for SMB vulnerabilities"""
        print(f"{Fore.YELLOW}[*] Checking SMB vulnerabilities...")
        # Check for known SMB vulnerabilities (EternalBlue, etc.)
        print(f"{Fore.YELLOW}[*] SMB vulnerability check requires additional tools")

    def check_mysql_vulnerabilities(self):
        """Check for MySQL vulnerabilities"""
        print(f"{Fore.YELLOW}[*] Checking MySQL vulnerabilities...")
        # Check for default credentials, outdated versions, etc.
        print(f"{Fore.YELLOW}[*] MySQL vulnerability check requires additional tools")

    def nmap_scan(self):
        """Perform advanced scan using nmap"""
        print(f"{Fore.CYAN}[*] Running Nmap scan for detailed information...")
        try:
            import nmap
            nm = nmap.PortScanner()
            nm.scan(self.target, arguments='-sV -sC -O')
            
            for host in nm.all_hosts():
                if 'osmatch' in nm[host]:
                    for osmatch in nm[host]['osmatch'][:1]:
                        self.results['os_info'] = osmatch['name']
                        print(f"{Fore.GREEN}[+] OS Detection: {osmatch['name']}")
                
                if 'tcp' in nm[host]:
                    for port in nm[host]['tcp']:
                        service_info = nm[host]['tcp'][port]
                        if port not in self.results['services']:
                            self.results['services'][port] = {
                                'service': service_info.get('name', 'Unknown'),
                                'version': service_info.get('version', ''),
                                'product': service_info.get('product', ''),
                                'banner': service_info.get('extrainfo', '')
                            }
        except ImportError:
            print(f"{Fore.YELLOW}[!] Python-nmap not installed. Skipping Nmap scan.")
        except Exception as e:
            print(f"{Fore.RED}[-] Nmap scan error: {e}")

    def network_recon(self):
        """Perform network reconnaissance"""
        print(f"{Fore.CYAN}[*] Performing network reconnaissance...")
        
        # Get host information
        try:
            host_info = socket.gethostbyaddr(self.target)
            self.results['network_info'] = {
                'hostname': host_info[0],
                'aliases': host_info[1],
                'ip': host_info[2][0]
            }
            print(f"{Fore.GREEN}[+] Hostname: {host_info[0]}")
        except:
            print(f"{Fore.YELLOW}[-] Could not resolve hostname")

    def generate_report(self):
        """Generate detailed report"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}SCAN REPORT")
        print(f"{Fore.CYAN}{'='*60}")
        
        print(f"{Fore.WHITE}Target: {Fore.YELLOW}{self.target}")
        print(f"{Fore.WHITE}Scan Time: {Fore.YELLOW}{self.results['scan_time']}")
        
        if self.results.get('os_info'):
            print(f"{Fore.WHITE}Operating System: {Fore.YELLOW}{self.results['os_info']}")
        
        if self.results.get('network_info'):
            print(f"{Fore.WHITE}Hostname: {Fore.YELLOW}{self.results['network_info'].get('hostname', 'N/A')}")
        
        print(f"\n{Fore.WHITE}Open Ports: {Fore.YELLOW}{len(self.results['open_ports'])}")
        for port in self.results['open_ports']:
            service = self.common_ports.get(port, 'Unknown')
            banner = self.results['services'].get(port, {}).get('banner', '')
            print(f"  {Fore.GREEN}[{port}] {service} - {banner[:50]}")
        
        print(f"\n{Fore.WHITE}Vulnerabilities Found: {Fore.YELLOW}{len(self.results['vulnerabilities'])}")
        if self.results['vulnerabilities']:
            for vuln in self.results['vulnerabilities']:
                print(f"{Fore.RED}  [!] Port {vuln['port']}: {vuln['vulnerability']}")
                print(f"      {Fore.YELLOW}Severity: {vuln['severity']}")
                print(f"      {Fore.CYAN}Recommendation: {vuln['recommendation']}")
        
        # Save to file
        try:
            filename = f"scan_report_{self.target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(self.results, f, indent=2)
            print(f"\n{Fore.GREEN}[+] Report saved to: {filename}")
        except Exception as e:
            print(f"{Fore.RED}[-] Could not save report: {e}")

    def run(self):
        """Main execution method"""
        self.banner()
        
        try:
            # Step 1: Network reconnaissance
            self.network_recon()
            
            # Step 2: Port scanning
            open_ports = self.port_scan()
            
            if not open_ports:
                print(f"{Fore.YELLOW}[!] No open ports found. The target may be down or protected.")
                return
            
            # Step 3: Advanced vulnerability scanning
            self.advanced_vulnerability_scan()
            
            # Step 4: Generate report
            self.generate_report()
            
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Scan interrupted by user.")
            sys.exit(0)
        except Exception as e:
            print(f"{Fore.RED}[-] Error: {e}")

def main():
    """Main function with argument parsing"""
    parser = argparse.ArgumentParser(description='Network Vulnerability Scanner for Kali Linux')
    parser.add_argument('target', help='Target IP address or hostname')
    parser.add_argument('-p', '--ports', help='Port range to scan (e.g., 1-1000)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Check if running on Kali Linux
    if not os.path.exists('/etc/kali-version'):
        print(f"{Fore.YELLOW}[!] Warning: This tool is optimized for Kali Linux")
    
    # Create scanner instance
    scanner = NetworkVulnerabilityScanner(args.target)
    
    # Run the scanner
    scanner.run()

if __name__ == "__main__":
    # Check for root privileges
    if os.geteuid() != 0:
        print(f"{Fore.RED}[-] This tool requires root privileges for full functionality.")
        print(f"{Fore.YELLOW}[!] Run with: sudo python3 {sys.argv[0]} [target]")
        sys.exit(1)
    
    main()
