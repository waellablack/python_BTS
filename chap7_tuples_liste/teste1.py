packets = [(500, 'TCP'),(1000, 'UDP'),(2000, 'TCP'),(50, 'ICMP'),(1600, 'TCP'),(800, 'UDP')]
print(packets)

print("\nPaquets dépassant 1500 octets :")
paquets_grands = [paquet for paquet in paquets if paquet[0] > 1500]
for paquet in paquets_grands:
    print(paquets_grands)

# 3. Pourcentage TCP et UDP
total = len(packets)
tcp_count = sum(1 for _, p in packets if p == 'TCP')
udp_count = sum(1 for _, p in packets if p == 'UDP')

print(f"\nPourcentage TCP : {tcp_count / total * 100:.2f}%")
print(f"Pourcentage UDP : {udp_count / total * 100:.2f}%")
