import logging
import os

os.makedirs("logs", exist_ok=True)

file_logger = logging.getLogger("file")

file_handler = logging.FileHandler(
    "logs/file_events.log"
)

file_logger.addHandler(file_handler)
file_logger.setLevel(logging.INFO)

def log_event(message):

    file_logger.info(message)

    print(message)
