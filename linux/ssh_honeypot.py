import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 2222

def log_attempt(ip, username, password):

    with open("logs/ssh_attempts.log", "a") as f:

        f.write(
            f"{datetime.now()} | "
            f"IP={ip} | "
            f"USER={username} | "
            f"PASS={password}\n"
        )

def start_ssh_honeypot():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind((HOST, PORT))
    server.listen(5)

    print(f"SSH Honeypot listening on {PORT}")

    while True:

        client, addr = server.accept()

        ip = addr[0]

        print(f"[CONNECTION] {ip}")

        client.send(
            b"Fake SSH Server\nUsername: "
        )

        username = client.recv(
            1024
        ).decode().strip()

        client.send(
            b"Password: "
        )

        password = client.recv(
            1024
        ).decode().strip()

        print(
            f"[LOGIN ATTEMPT] "
            f"{ip} "
            f"{username}:{password}"
        )

        log_attempt(
            ip,
            username,
            password
        )

        client.send(
            b"Authentication failed\n"
        )

        client.close()
