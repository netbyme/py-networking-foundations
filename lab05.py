# Lab 05 - Validate IP Format
# Concepts: if/else, conditions, len(), split(), isdigit(), all()
ip_list = ["192.168.1.1", "192.168.9.0.0", "abc.def.ghi.jkl", "192.168"]

# Loop through each IP
for ip in ip_list:

    # Split the IP by "." to get each octet
    parts = ip.split(".")

    # Check 1: must have exactly 4 parts
    # Check 2: every part must be a number (isdigit)
    # all() returns True only if every part passes the check
    if len(parts) == 4 and all(part.isdigit() for part in parts):
        print(f"{ip} →  valid")
        
    # If any check fails → Invalid
    else: 
        print(f"{ip} → Invalid")