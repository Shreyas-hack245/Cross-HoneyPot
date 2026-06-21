from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    try:
        with open("logs/events.log", "r") as f:
            logs = f.readlines()

    except Exception:
        logs = ["No events logged yet"]

    html = f"""
    <html>
    <head>
        <title>Cross-HoneyPot Dashboard</title>

        <style>

            body {{
                background-color: #111;
                color: #00ff00;
                font-family: monospace;
                padding: 20px;
            }}

            h1 {{
                text-align: center;
            }}

            .log {{
                border: 1px solid #00ff00;
                padding: 10px;
                margin: 5px;
                border-radius: 5px;
            }}

        </style>

    </head>

    <body>

        <h1>🛡 Cross-HoneyPot Dashboard</h1>

        <h2>Recent Events</h2>

        {''.join([f"<div class='log'>{log}</div>" for log in reversed(logs)])}

    </body>

    </html>
    """

    return html


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
