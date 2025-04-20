import re
from datetime import datetime

def parse_ssh_log(filepath):
    logs = []

    with open(filepath, 'r') as file:
        for line in file:
            try:
                parts = line.split()
                timestamp = datetime.strptime(" ".join(parts[0:3]), "%b %d %H:%M:%S")
                ip = parts[-4]
                message = " ".join(parts[4:])
                logs.append({
                    "timestamp": timestamp,
                    "ip": ip,
                    "message": message
                })
            except Exception as e:
                print(f"Error parsing line: {line.strip()}")
                print(f"Exception: {e}")

    return logs