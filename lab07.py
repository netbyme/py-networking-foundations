# Lab 07 - Reusable Network Functions
# Instead of writing the same code over and over, I built 3 functions
# that I can call anytime I need them — cleaner and more professional

# ─── FUNCTIONS ───

# This function takes device info as input and returns a clean dictionary
# Useful when I need to create multiple devices without repeating code
def get_device_info(name, ip, device_type):
    device = {
        "name": name,
        "ip": ip,
        "device_type": device_type,
    }
    return device

# This function checks if an IP address is valid
# It splits the IP by "." and makes sure it has 4 numeric parts
# Returns True if valid, False if not — simple yes or no answer
def validate_ip(ip):
    parts = ip.split(".")
    if len(parts) == 4 and all(part.isdigit() for part in parts):
        return True
    return False

# This function loops through a list of devices and prints each one
# I pass the whole list in and it handles the rest automatically

def print_inventory(devices):
    print("=== Network Inventory ===")
    for index, device in enumerate(devices, start=1):
        print(f"[{index}] Name: {device['name']} | IP: {device['ip']} | Type: {device['device_type']}")

# ─── USE FUNCTIONS ───

# Building my device list by calling get_device_info for each device
# Much cleaner than creating each dictionary manually
devices = [
    get_device_info("Router01", "192.168.1.1", "Router"),
    get_device_info("Switch01", "192.168.1.2", "Switch"),
    get_device_info("Firewall01", "192.168.1.3", "Firewall"),
]

# Validate each IP before doing anything with the device
# Good habit in real network scripts always check before connecting
for device in devices:
    result = validate_ip(device["ip"])
    print(f"{device['ip']} → {'Valid' if result else 'Invalid'}")

print_inventory(devices)