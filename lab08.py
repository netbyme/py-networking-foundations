# Lab 08 - Match IPs to Hostnames using zip()
# I used to wonder how scripts handle two lists at the same time
# zip() solved that — it pairs them like two columns in a table

# ─── DATA ───

# These are my devices — just names, nothing else
names = ["Router01", "Switch01", "Firewall01"]

# Their IPs — same order as the names above, that's important
ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

# Current status of each device — who's up, who's down
statuses = ["Active", "Inactive", "Active"]

# ─── PAIRING THEM TOGETHER ───

# zip() reads all three lists at the same time, row by row
# without zip I would have to use index numbers manually — messy
active_count = 0

for name, ip, status in zip(names, ips, statuses):
    print(f"{name} | {ip} | {status}")
    
    # every time I find an active device I add 1 to the counter
    if status == "Active":
        active_count += 1

# ─── REPORT ───

# after the loop I know exactly how many devices are alive
print(f"\nTotal active devices: {active_count}")

