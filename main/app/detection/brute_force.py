from datetime import datetime, timedelta
from collections import defaultdict

def detect_brute_force(logs,threshold=5,time_window_minutes=2):
    failed_attempts = defaultdict(list)
    incidents = []

    for log in logs:
        if "Failed password" in log["message"]:
            ip = log["ip"]
            timestamp = log["timestamp"]
            failed_attempts[ip].append(timestamp)
        # Remove timestamps outside the time window

    for ip, timestamps in failed_attempts.items():
        timestamps.sort()

        for i in range(len(timestamps)):
            count = 1
            for j in range(i + 1, len(timestamps)):
                if (timestamps[j] - timestamps[i]) <= timedelta(minutes=time_window_minutes):
                    count += 1
                else:
                    break
            if count >= threshold:
                incidents.append({
                    "type": "Brute Force Attack",
                    "srouce_ip": ip,
                    "failed_attempts": count,
                    "time_window_start": timestamps[i],
                    "time_window_end": timestamps[i] + timedelta(minutes=time_window_minutes),
                    "status": "suspicious"
                })
                break

    return incidents