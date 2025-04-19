import re

def parse_logs(raw_logs):
    parsed = []

    log_pattern = re.compile(
        r'^(?P<timestamp>\w{3} +\d{1,2} +\d{2}:\d{2}:\d{2}) (?P<host>\S+) (?P<service>\S+\[\d+\]): (?P<message>.+)$'
    )
    ip_pattern = re.compile(r'from ([\d\.]+) port')

    for line in raw_logs:
        match = log_pattern.match(line)
        if match:
            entry = match.groupdict()
            ip_match = ip_pattern.search(entry["message"])
            if ip_match:
                entry["ip"] = ip_match.group(1)
            parsed.append(entry)

    return parsed
