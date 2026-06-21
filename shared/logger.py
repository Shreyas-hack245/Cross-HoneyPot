from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)

def log_event(message):

    timestamp = datetime.now()

    log = f"{timestamp} | {message}"

    print(log)

    with open(
        "logs/events.log",
        "a"
    ) as file:

        file.write(log + "\n")
