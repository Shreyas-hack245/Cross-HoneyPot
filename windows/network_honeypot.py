import socket

from shared.logger import log_event
from shared.threat_scoring import add_score

HOST = "0.0.0.0"
PORT = 2223


def start_network_honeypot():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind((HOST, PORT))
    server.listen(5)

    print(
        f"Windows Honeypot listening on {PORT}"
    )

    while True:

        client, addr = server.accept()

        score = add_score("network")

        event = (
            f"[WINDOWS CONNECTION] "
            f"IP={addr[0]} "
            f"SCORE={score}"
        )

        log_event(event)

        client.send(
            b"Unauthorized Access\n"
        )

        client.close()
