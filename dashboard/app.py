from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    try:

        with open("logs/events.log", "r") as file:
            logs = file.readlines()

    except:
        logs = ["No events yet"]

    html = """
    <html>
    <head>
        <title>Cross-HoneyPot Dashboard</title>
    </head>

    <body>

        <h1>Cross-HoneyPot Dashboard</h1>

        <h2>Recent Events</h2>

        <pre>
    """

    for log in reversed(logs[-20:]):
        html += log

    html += """

        </pre>

    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True)
