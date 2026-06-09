# Lab 09 - Read and Write Config Files

# Open a file and write device data into it
# "w" means write mode — creates the file if it doesn't exist
with open("devices.txt", "w") as f:
    f.write("Router01,192.168.1.1,Active\n")
    f.write("Switch01,192.168.1.2,Inactive\n")
    f.write("Firewall01,192.168.1.3,Active\n")

print("devices.txt created successfully!")

# Now read the file back line by line
# "r" means read mode
with open("devices.txt", "r") as f:
    for line in f:
        # strip() removes the \n at the end of each line
        # split(",") cuts the line into 3 parts by comma
        parts = line.strip().split(",")
        name = parts[0]
        ip = parts[1]
        status = parts[2]
        print(f"Name: {name} | IP: {ip} | Status: {status}")
        
# Write a report file summarizing the device status
with open("report.txt", "w") as f:
    f.write("=== Network Status Report ===\n")
    
    with open("devices.txt", "r") as devices:
        for line in devices:
            parts = line.strip().split(",")
            name = parts[0]
            ip = parts[1]
            status = parts[2]
            
            if status == "Active":
                f.write(f"[OK]   {name} | {ip} | {status}\n")
            else:
                f.write(f"[DOWN] {name} | {ip} | {status}\n")

print("report.txt created successfully!")