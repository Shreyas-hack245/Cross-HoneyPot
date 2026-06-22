import platform
import threading

if platform.system() == "Linux":

    from linux.file_monitor import start_file_monitor
    from linux.process_monitor import start_process_monitor
    from linux.ssh_honeypot import start_ssh_honeypot

    threads = [
        threading.Thread(target=start_file_monitor),
        threading.Thread(target=start_process_monitor),
        threading.Thread(target=start_ssh_honeypot)
    ]

elif platform.system() == "Windows":

    from windows.file_monitor import start_file_monitor
    from windows.process_monitor import start_process_monitor
    from windows.network_honeypot import start_network_honeypot

    threads = [
        threading.Thread(target=start_file_monitor),
        threading.Thread(target=start_process_monitor),
        threading.Thread(target=start_network_honeypot)
    ]

else:

    print("Unsupported OS")
    exit()

for t in threads:
    t.start()

for t in threads:
    t.join()
