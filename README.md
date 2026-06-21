# Cross-HoneyPot

Cross-HoneyPot is a lightweight Linux-based honeypot and monitoring system developed for cybersecurity learning and research.

## Features

* File Monitoring
* Process Monitoring
* SSH Honeypot
* Threat Scoring
* Event Logging
* Flask Dashboard

## Project Structure

```text
Cross-HoneyPot/
├── dashboard/
├── honeypot_files/
├── linux/
├── shared/
├── logs/
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

Start the monitoring system:

```bash
python3 main.py
```

Start the dashboard:

```bash
python3 dashboard/app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Detection Capabilities

* Detects suspicious tools such as:

  * Nmap
  * Hydra
  * SQLMap
  * Hashcat
  * Wireshark

* Logs file modifications in honeypot files.

* Records SSH login attempts.

## Technologies Used

* Python
* Flask
* Psutil
* Watchdog

## Future Work

* Windows Support
* Database Integration
* Email Alerts
* Advanced Dashboard Analytics

## Disclaimer

This project is intended for educational and defensive security purposes only.
