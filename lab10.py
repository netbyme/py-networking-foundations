# Lab 10 - Filter Active Devices
# Concepts: list comprehension, filter()

# List of devices with mixed statuses
devices = [
    {"name": "Router01", "ip": "192.168.1.1", "status": "Active"},
    {"name": "Switch01", "ip": "192.168.1.2", "status": "Inactive"},
    {"name": "Firewall01", "ip": "192.168.1.3", "status": "Active"},
    {"name": "Switch02", "ip": "192.168.1.4", "status": "Inactive"},
    {"name": "Router02", "ip": "192.168.1.5", "status": "Active"},
]

# Filter only active devices using list comprehension
active_devices = [device for device in devices if device["status"] == "Active"]

# Print active devices
print("=== Active Devices ===")
for device in active_devices:
    print(f"{device['name']} | {device['ip']} | {device['status']}")

print(f"\nTotal active: {len(active_devices)}")