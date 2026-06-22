# Cross-HoneyPot

Cross-HoneyPot is a lightweight cross-platform cybersecurity honeypot and host monitoring framework built for educational and research purposes. The project helps detect suspicious activities on Linux and Windows systems through process monitoring, file monitoring, threat scoring, and deception-based honeypot services.

## Features

### Linux

* File Monitoring Honeypot
* Process Monitoring
* SSH Honeypot
* Threat Scoring
* Centralized Event Logging

### Windows

* File Monitoring
* Process Monitoring
* Network Honeypot
* Threat Scoring
* Centralized Event Logging

### Dashboard

* Real-time Event Viewing
* Timestamped Security Logs
* Flask-Based Web Interface

## Project Structure

Cross-HoneyPot/

├── dashboard/

│   └── app.py

├── honeypot_files/

│   ├── Admin_Credentials.txt

│   ├── Bank_Details.txt

│   └── Passwords.txt

├── linux/

│   ├── file_monitor.py

│   ├── process_monitor.py

│   ├── ssh_honeypot.py

│   └── network_honeypot.py

├── windows/

│   ├── file_monitor.py

│   ├── process_monitor.py

│   └── network_honeypot.py

├── shared/

│   ├── logger.py

│   ├── threat_scoring.py

│   └── config.py

├── logs/

├── main.py

├── requirements.txt

└── README.md

## Installation

Clone the repository:

```bash
git clone https://github.com/Shreyas-hack245/Cross-HoneyPot.git
cd Cross-HoneyPot
```

Create a virtual environment:

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Cross-HoneyPot

Start all monitoring modules automatically:

```bash
python main.py
```

The framework automatically detects the operating system and loads the appropriate modules.

## Dashboard

Launch the dashboard:

```bash
python dashboard/app.py
```

Open:

http://127.0.0.1:5000

## Detection Capabilities

Cross-HoneyPot can detect activity from commonly used security assessment and attack tools such as:

* Nmap
* Hydra
* SQLMap
* Hashcat
* John The Ripper
* Wireshark
* Aircrack-ng

The framework also monitors honeypot files and records unauthorized access attempts.

## Logging

All security events are stored in:

```text
logs/events.log
```

Example:

```text
2026-06-22 21:30:11 | [WINDOWS ALERT] nmap.exe PID=1234 SCORE=20

2026-06-22 21:35:42 | [SSH ATTEMPT] USER=admin PASS=password

2026-06-22 21:40:18 | [FILE MODIFIED] honeypot_files/Passwords.txt
```

## Technologies Used

* Python
* Flask
* Psutil
* Watchdog
* Socket Programming
* Git & GitHub

## Future Enhancements

* SQLite Database Integration
* Email Alerts
* Advanced Dashboard Analytics
* Docker Deployment
* Threat Intelligence Integration

## Disclaimer

This project is intended for educational, research, and defensive cybersecurity purposes only. Use responsibly and only on systems you own or are authorized to test.

## Author

Shreyas Bhat

B.Tech Computer Science Engineering

Cybersecurity Enthusiast
