from scapy.all import rdpcap, ICMP

# reorder using reordercap in wsl run this command --> 'reordercap network.pcap network_sorted.pcap'

PCAP_FILE = 'network_sorted.pcap'
OUTPUT_FILE = 'output.png'

with open(OUTPUT_FILE, 'wb') as f:    
    packets = rdpcap(PCAP_FILE)
    for packet in packets:                
        if ICMP in packet and packet[ICMP].type == 8:  #Type 8 ==> ICMP request data
            chunk = packet[ICMP].load # Load the data only of the ICMP packet
            f.write(chunk)