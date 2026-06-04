# Lab 06 - Classify IP Ranges
# Concepts: if/elif/else, int(), IP classes A/B/C/D

# List of IPs from different classes to test
ip_list = ["192.168.1.1", "10.0.0.1", "172.16.0.1", "224.0.0.1", "256.1.1.1"]

# Loop through each IP
for ip in ip_list:

    # Split IP by "." to get each octet
    parts = ip.split(".")

    # First check: valid format - 4 parts and all digits
    if len(parts) == 4 and all(part.isdigit() for part in parts):

    # Convert first octet from string to number for comparison
        first = int (parts[0])


        # Classify based on first octet range
        if first >= 1 and first <= 126:
            print(f"{ip} → class A")
        elif first >= 128 and first <= 191:
            print(f"{ip} → class B")
        elif first >= 192 and first <= 223:
            print(f"{ip} → class C")
        elif first >= 224 and first <= 239:
            print(f"{ip} → class D")

        # First octet exists but outside all class ranges
        else:
            print(f"{ip} → Invalid Range")
    # IP format is wrong - missing octets or contains letters
    else:
        print(f"{ip} → Invalid Format")