THREAT_SCORE = 0

EVENT_SCORES = {
    "file_access": 10,
    "nmap": 20,
    "hydra": 40,
    "sqlmap": 35,
    "ssh_attempt": 30
}

def add_score(event):
    global THREAT_SCORE

    THREAT_SCORE += EVENT_SCORES.get(event, 5)

    return THREAT_SCORE

def get_score():
    return THREAT_SCORE

def get_level():

    score = get_score()

    if score < 20:
        return "LOW"

    elif score < 60:
        return "MEDIUM"

    return "HIGH"
