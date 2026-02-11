import sys
from pathlib import Path
 
error_ip = 0
try:
    ip = sys.argv[1]
except IndexError:
    print(f"Error: Please Provide Ip Address.")
    print(f"usage: python logscanner.py <IP_ADDRESS>")
    sys.exit(1)

print(f"Scanning log file for IP: {ip}...")

with open("server.log", "r") as log_file, open("security_log.text", "w") as report_file:

    report_file.write(f"security report for {ip}\n")

    for line in log_file:

        if ip in line:
            error_ip += 1

        if "ERROR"  in line:
            report_file.write(line.strip() + "\n")


        elif "CRITICAL" in line:
            report_file.write(line.strip() + "\n")

    # Visual separator and summary must be written before the files are closed
    report_file.write("-" * 30 + "\n")
    report_file.write(f"SUMMARY: Found {error_ip} events related to IP {ip}\n")


