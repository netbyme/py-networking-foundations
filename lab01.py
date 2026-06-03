#Lab01 - Device Inventory Basics  

#List of devices in the network inventory 

device_name = ["Router01", "Switch01", "Firewall01"]
IP_address = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
device_type = ["Router", "Switch", "Firewall"]
status = ["Active", "Active", "Offline"]
#loop using enumerate to print the index and device name 
for index, device in enumerate(device_name):
    print(index, device, IP_address[index], device_type[index], status[index])

