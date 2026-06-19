import psutil
import time

def start_process_monitor():

    print("Process monitor started...")

    while True:

        for proc in psutil.process_iter(['pid', 'name']):
            try:
                print(proc.info['name'])
            except:
                pass

        time.sleep(5)
