from app.detection.brute_force import detect_brute_force
#add the rest of the detections here

def run_all_rules(logs):

    """
    Run all detection rules on the provided logs.
    """

    # Add all detection functions here
    all_incidents = []
    
    # Brute Force Detection
    brute_force_detections = detect_brute_force(logs)
    all_incidents.extend(brute_force_detections)
    
    # Add other detection functions here
    # e.g., detections.extend(detect_sql_injection(logs))
    
    return all_incidents