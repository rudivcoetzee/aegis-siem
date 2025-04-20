from app.parsers.log_parser import parse_ssh_log
from detectors.rule_engine import run_all_rules
# this is to test the all the detectors


def main():
    logs = parse_ssh_log("example_logs/ssh.log")
    print(f"Parsed {len(logs)} logs.")

    incidents = run_all_rules(logs)

    print("Detected Incidents:")
    for incident in incidents:
        print(incident)

if __name__ == "__main__":
    main()

