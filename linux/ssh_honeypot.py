import socket
from datetime import datetime

from shared.logger import log_event
from shared.threat_scoring import add_score

HOST = "0.0.0.0"
PORT = 2222


def start_ssh_honeypot():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind((HOST, PORT))
    server.listen(5)

    print(
        f"SSH Honeypot listening on port {PORT}"
    )

    while True:

        client, addr = server.accept()

        ip = addr[0]

        client.send(
            b"Username: "
        )

        username = (
            client.recv(1024)
            .decode()
            .strip()
        )

        client.send(
            b"Password: "
        )

        password = (
            client.recv(1024)
            .decode()
            .strip()
        )

        score = add_score(
            "ssh_attempt"
        )

        event = (
            f"[SSH ATTEMPT] "
            f"IP={ip} "
            f"USER={username} "
            f"PASS={password} "
            f"SCORE={score}"
        )

        log_event(event)

        client.send(
            b"Authentication failed\n"
        )

        client.close()
