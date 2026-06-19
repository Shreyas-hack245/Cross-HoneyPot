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

                if name and name.lower() in SUSPICIOUS_TOOLS:

                    unique_id = f"{name}_{proc.info['pid']}"

                    if unique_id not in detected:

                        detected.add(unique_id)

                        log_event(
                            f"[SUSPICIOUS PROCESS] "
                            f"{name} "
                            f"PID={proc.info['pid']}"
                        )

            except:
                pass

        time.sleep(3)
