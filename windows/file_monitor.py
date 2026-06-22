from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from shared.logger import log_event

import time


class HoneyPotHandler(FileSystemEventHandler):

    def on_modified(self, event):

        if not event.is_directory:

            log_event(
                f"[WINDOWS FILE MODIFIED] "
                f"{event.src_path}"
            )


def start_file_monitor():

    path = "honeypot_files"

    observer = Observer()

    observer.schedule(
        HoneyPotHandler(),
        path,
        recursive=True
    )

    observer.start()

    print("Windows File Monitor Started")

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()
