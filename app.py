from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask 2025-01-01 16:32"
