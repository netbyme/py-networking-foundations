#Lab02 using dictionarie for Devices Inventory Basics 

devices = [
    {"name": "Router01", "IP": "192.168.1.1", "type": "Router", "status": "Active"},
    {"name": "Switch01", "IP": "192.168.1.2", "type": "Switch", "status": "Active"},
    {"name": "Firewall01", "IP": "192.168.1.3", "type": "Firewall", "status": "Active"}
]

#Loop through the devices dictionary and print the device name and its details 
for index, device in enumerate(devices, start=1):
    print(f"[{index}] Name: {device['name']}, IP: {device['IP']}, Type: {device['type']}, status: {device['status']}")

