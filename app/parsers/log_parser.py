import re

def parse_logs(raw_logs):
    parsed = []

    log_pattern = re.compile(
        r'^(?P<timestamp>\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) (?P<host>\S+) (?P<service>\S+): (?P<message>.+)$'
    )

    for line in raw_logs:
        match = log_pattern.match(line)
        if match:
            parsed.append(match.groupdict())

    return parsed
