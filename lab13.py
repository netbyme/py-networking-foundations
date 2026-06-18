# Lab 13 - Handle Connection Errors
# In real network scripts connections fail all the time
# try/except stops the script from crashing and handles errors gracefully

devices = [
    {"name": "Router01", "ip": "192.168.1.1"},
    {"name": "Switch01", "ip": "999.999.999.999"},  # invalid IP
    {"name": "Firewall01", "ip": "192.168.1.3"},
    {"name": "Router02", "ip": ""},  # empty IP
]

def connect_to_device(device):
    ip = device["ip"]
    name = device["name"]
    
    try:
        # check if IP is empty before doing anything
        if not ip:
            raise ValueError("IP address is empty")
        
        # split the IP and check it has exactly 4 parts
        parts = ip.split(".")
        if len(parts) != 4:
            raise ValueError(f"Invalid IP format: {ip}")
        
        # check every octet is a number between 0 and 255
        # if any octet fails this check we raise an error immediately
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                raise ValueError(f"Octet out of range: {ip}")
        
        # only reaches here if ALL checks passed
        print(f"[OK] Connected to {name} at {ip}")
    
    # if any error was raised above — catch it here and print it
    # the script keeps running instead of crashing
    except ValueError as e:
        print(f"[ERROR] Could not connect to {name} — {e}")

# loop through all devices and attempt connection
print("=== Connection Attempts ===")
for device in devices:
    connect_to_device(device)