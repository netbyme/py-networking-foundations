# Lab 14 - Read CSV Device List
# In real networks device lists are often stored in CSV files
# Instead of hardcoding devices I read them from a file — more professional

import csv

# First create a sample CSV file with device data
with open("devices.csv", "w", newline="") as f:
    writer = csv.writer(f)
    
    # write the header row
    writer.writerow(["name", "ip", "type", "status"])
    
    # write device rows
    writer.writerow(["Router01", "192.168.1.1", "Router", "Active"])
    writer.writerow(["Switch01", "192.168.1.2", "Switch", "Inactive"])
    writer.writerow(["Firewall01", "192.168.1.3", "Firewall", "Active"])
    writer.writerow(["Router02", "192.168.1.4", "Router", "Active"])
    writer.writerow(["Switch02", "192.168.1.5", "Switch", "Inactive"])

print("devices.csv created!")

# Now read the CSV file back
print("\n=== Device List from CSV ===")

with open("devices.csv", "r") as f:
    reader = csv.DictReader(f)
    
    for device in reader:
        print(f"{device['name']} | {device['ip']} | {device['type']} | {device['status']}")