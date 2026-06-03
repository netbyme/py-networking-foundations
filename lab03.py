# Lab 03 - Store Device Info using Dictionary Methods

# Create a dictionary to store a single device profile
device =  {"name": "Router_001", "ip": "192.168.1.1", "type": "Router", "status": "Active", "Location": "Casablanca_siege"}

# Print all keys in the dictionary
print("keys:", list(device.keys()))

# Print all values in the dictionary
print("values:", list(device.values()))

print("----")

# Loop through key-value pairs and print each one
for key,value in device.items():
    print(f"{key}→ {value}")