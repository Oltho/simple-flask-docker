from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    flask_host: str = os.getenv("FLASK_HOST", default="localhost")
    flask_port: int = os.getenv("FLASK_PORT", default=8080)
    flask_debug: bool = (os.getenv("FLASK_DEBUG", default="false").lower == "true")

    app.run(host=flask_host, port=flask_port, debug=flask_debug)
