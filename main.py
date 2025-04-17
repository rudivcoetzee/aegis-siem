from app.parsers.log_parser import parse_logs

# testing the log parser

# this is to read the log file
with open ("example_logs/ssh.log", "r") as f:
    raw_logs = f.readlines()

# this is to parse the log file
parsed_logs = parse_logs(raw_logs)

# this is to print the parsed log file
for log in parsed_logs:
    print(log)

