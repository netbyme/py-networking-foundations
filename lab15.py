# Lab 15 - Generate Network Inventory Report
# This is the capstone lab — it combines everything I built across all 14 labs
# reads devices from CSV, validates IPs, filters active devices, writes a report

import csv

# ─── FUNCTIONS ───

# validate IP address — from Lab 13
def validate_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

# generate and save the full report
def generate_report(devices, filename="inventory_report.txt"):
    active = [d for d in devices if d["status"] == "Active"]
    inactive = [d for d in devices if d["status"] == "Inactive"]
    invalid = [d for d in devices if not validate_ip(d["ip"])]

    with open(filename, "w") as f:
        f.write("=== Network Inventory Report ===\n\n")

        f.write(f"Total devices   : {len(devices)}\n")
        f.write(f"Active devices  : {len(active)}\n")
        f.write(f"Inactive devices: {len(inactive)}\n")
        f.write(f"Invalid IPs     : {len(invalid)}\n")
        f.write("\n")

        f.write("─── Device List ───\n")
        for i, device in enumerate(devices, start=1):
            status_tag = "[OK]  " if device["status"] == "Active" else "[DOWN]"
            ip_tag = "" if validate_ip(device["ip"]) else " [INVALID IP]"
            f.write(f"{i}. {status_tag} {device['name']} | {device['ip']}{ip_tag} | {device['type']}\n")

        f.write("\n─── Active Devices ───\n")
        for device in active:
            f.write(f"  {device['name']} | {device['ip']}\n")

        f.write("\n─── Issues Found ───\n")
        for device in inactive:
            f.write(f"  [DOWN] {device['name']} | {device['ip']}\n")
        for device in invalid:
            f.write(f"  [INVALID IP] {device['name']} | {device['ip']}\n")

    print(f"Report saved to {filename}")

# ─── MAIN ───

# read devices from CSV — from Lab 14
devices = []
with open("devices.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        devices.append(row)

# generate the report
generate_report(devices)

# print summary to terminal
print(f"\nTotal devices: {len(devices)}")
print(f"Active: {len([d for d in devices if d['status'] == 'Active'])}")
print(f"Inactive: {len([d for d in devices if d['status'] == 'Inactive'])}")