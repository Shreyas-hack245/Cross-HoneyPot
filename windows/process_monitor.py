import psutil
import time

from shared.logger import log_event
from shared.threat_scoring import add_score

SUSPICIOUS_TOOLS = [
    "nmap.exe",
    "wireshark.exe",
    "sqlmap.exe",
    "hydra.exe"
]

detected = set()

def start_process_monitor():

    print("Windows Process Monitor Started")

    while True:

        for proc in psutil.process_iter(
            ['pid', 'name']
        ):

            try:

                name = proc.info['name']

                if not name:
                    continue

                name = name.lower()

                if name in SUSPICIOUS_TOOLS:

                    uid = (
                        f"{name}_{proc.info['pid']}"
                    )

                    if uid not in detected:

                        detected.add(uid)

                        score = add_score("nmap")

                        alert = (
                            f"[WINDOWS ALERT] "
                            f"{name} "
                            f"PID={proc.info['pid']} "
                            f"SCORE={score}"
                        )

                        log_event(alert)

            except:
                pass

        time.sleep(0.1)