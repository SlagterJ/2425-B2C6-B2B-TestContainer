from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "All systems operational. V1.0"
