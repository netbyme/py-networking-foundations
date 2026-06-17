# Lab 11 - Transform Device Data
# Concepts: map(), lambda

# Device list
devices = [
    {"name": "Router01", "ip": "192.168.1.1", "status": "Active"},
    {"name": "Switch01", "ip": "192.168.1.2", "status": "Inactive"},
    {"name": "Firewall01", "ip": "192.168.1.3", "status": "Active"},
]

# Extract all names using map + lambda
names = list(map(lambda d: d["name"], devices))

# Extract all IPs using map + lambda
ips = list(map(lambda d: d["ip"], devices))

# Add prefix to every name
labeled = list(map(lambda d: "[Device:] " + d["name"], devices))

# Print results
print("Names:", names)
print("IPs:", ips)
print("Labeled:", labeled)