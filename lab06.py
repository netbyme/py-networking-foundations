

ip_list = ["192.168.1.1", "10.0.0.1", "172.16.0.1", "224.0.0.1", "256.1.1.1"]

for ip in ip_list:
    parts = ip.split(".")
    first = int (parts[0])
    if first >= 1 and first <= 126:
        print(f"{ip} → class A")
    elif first >= 128 and first <= 191:
        print(f"{ip} → class B")
    elif first >= 192 and first <= 223:
        print(f"{ip} → class C")
    elif first >= 224 and first <= 239:
        print(f"{ip} → class D")
    else:
        print(f"{ip} → Invalid")