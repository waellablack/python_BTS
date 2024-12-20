logs = [
    ('192.168.1.1', '2024-09-12 12:15:10'),
    ('192.168.1.2', '2024-09-12 12:16:15'),
    ('192.168.1.1', '2024-09-12 12:20:20'),
    ('192.168.1.3', '2024-09-12 12:30:25'),
    ('192.168.1.1', '2024-09-12 12:35:30')
]

# 1. Identifier les adresses IP qui se sont connectées plus de 3 fois
ip_count = {}
for log in logs:
    ip = log[0]
    ip_count[ip] = ip_count.get(ip, 0) + 1

print("Adresses IP avec plus de 3 connexions :")
for ip, count in ip_count.items():
    if count > 3:
        print(f"{ip}: {count} connexions")

# 2. Trouver l'adresse IP qui s'est connectée en premier et celle qui s'est connectée en dernier
first_connection = min(logs, key=lambda x: x[1])
last_connection = max(logs, key=lambda x: x[1])

print(f"\nPremière connexion : {first_connection[0]} à {first_connection[1]}")
print(f"Dernière connexion : {last_connection[0]} à {last_connection[1]}")

# 3. Compter le nombre total d'adresses IP uniques
unique_ips = set(ip_count.keys())
print(f"\nNombre total d'adresses IP distinctes : {len(unique_ips)}")
