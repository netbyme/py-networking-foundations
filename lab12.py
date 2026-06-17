# Lab 12 - Parse Network Log Files
# I'm reading a log file and extracting only errors and warnings
# This is something NOC engineers do manually every day — I'm automating it

# First create a sample log file to work with
with open("network.log", "w") as f:
    f.write("INFO: Router01 is up\n")
    f.write("WARNING: High CPU on Switch01\n")
    f.write("INFO: Firewall01 connection established\n")
    f.write("ERROR: Router02 is unreachable\n")
    f.write("INFO: Switch02 is up\n")
    f.write("ERROR: Firewall02 authentication failed\n")
    f.write("WARNING: Low memory on Router01\n")

print("network.log created!")

# Now read the log file and extract only problems
print("\n=== Network Issues Found ===")

errors = []
warnings = []

with open("network.log", "r") as f:
    for line in f:
        line = line.strip()
        
        # check if line is an error
        if line.startswith("ERROR"):
            errors.append(line)
            print(f"[ERROR]   {line}")
        
        # check if line is a warning
        elif line.startswith("WARNING"):
            warnings.append(line)
            print(f"[WARNING] {line}")

# Summary report
print(f"\nTotal errors: {len(errors)}")
print(f"Total warnings: {len(warnings)}")
print(f"Total issues: {len(errors) + len(warnings)}")