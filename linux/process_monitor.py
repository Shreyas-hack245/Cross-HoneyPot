import psutil
import time
from shared.logger import log_event

SUSPICIOUS_TOOLS = [
    "nmap",
    "hydra",
    "john",
    "hashcat",
    "sqlmap",
    "wireshark",
    "aircrack-ng"
]

detected = set()

def start_process_monitor():

    print("Process monitor started...")

    while True:

        for proc in psutil.process_iter(['pid', 'name']):

            try:
                name = proc.info['name']

                if not name:
                    continue

                name = name.lower()

                if name in SUSPICIOUS_TOOLS:

                    unique_id = f"{name}_{proc.info['pid']}"

                    if unique_id not in detected:

                        detected.add(unique_id)

                        alert = (
                            f"[ALERT] Suspicious Process: "
                            f"{name} PID={proc.info['pid']}"
                        )

                        print(alert)
                        log_event(alert)

            except Exception:
                pass

        time.sleep(0.1)
