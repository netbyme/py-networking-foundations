# Lab 04 - Parse IP Addresses
# Concepts: strings, split(), len(), f-strings

# List of IP addresses to parse
ip_list = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

# Loop through each IP address
for ip in ip_list:
        # Split the IP by "." to get each octet as a list  
    parts = ip.split(".")

    # Print the full IP
    print(f"IP: {ip}")

    # Print each octet using its index position
    print(f"   octet 1: {parts[0]}")
    print(f"   octet 2: {parts[1]}")
    print(f"   octet 3: {parts[2]}")
    print(f"   octet 4: {parts[3]}")
    print(f"   Total parts: {len(parts)}")
    print("---")