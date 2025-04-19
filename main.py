from app.parsers.log_parser import parse_logs
from app.detection.brute_force import detect_brute_force

# testing the log parser

# this is to read the log file
with open ("example_logs/ssh.log", "r") as f:
    raw_logs = f.readlines()

# this is to parse the log file
parsed_logs = parse_logs(raw_logs)

incidents = detect_brute_force(parsed_logs)
# this is to print the incidents
for incident in incidents:
    print(incident)
# this is to print the raw log file