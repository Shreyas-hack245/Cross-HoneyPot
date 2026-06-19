import platform

if platform.system() == "Linux":
    from linux.file_monitor import start_monitor

elif platform.system() == "Windows":
    from windows.file_monitor import start_monitor

else:
    print("Unsupported OS")
    exit()

start_monitor()
