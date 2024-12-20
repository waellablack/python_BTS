paquets = [(500, 'TCP') , (1000, 'UDP') , (2000, 'TCP') , (50, 'ICMP') , (1600, 'TCP') , (800, 'UDP')]
print(paquets)

print("\nPaquets dépassant 1500 octets :")
paquets_grands = [paquet for paquet in paquets if paquet[0] > 1500]
tcp = 0
icmp = 0
udp = 0
tcp_liste = []
icmp_liste = []
udp_liste = []
print(paquets_grands)
for paquet in paquets:
    if "TCP" in paquet:
        tcp_liste.append(paquet)
        tcp += 1
pourecentage_tcp = tcp / 6 * 100  
print(f"{pourecentage_tcp}%")
for paquet in paquets:
    if "ICMP" in paquet:
        icmp_liste.append(paquet)
        icmp += 1
pourecentage_icmp = icmp / 6 * 100  
print(f"{pourecentage_icmp}%")
for paquet in paquets:
    if "UDP" in paquet:
        udp_liste.append(paquet)
        udp += 1
pourecentage_udp = udp / 6 * 100  
print(f"{pourecentage_udp}%")

