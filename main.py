import threading

from linux.process_monitor import (
    start_process_monitor
)

from linux.ssh_honeypot import (
    start_ssh_honeypot
)

t1 = threading.Thread(
    target=start_process_monitor
)

t2 = threading.Thread(
    target=start_ssh_honeypot
)

t1.start()
t2.start()

t1.join()
t2.join()
