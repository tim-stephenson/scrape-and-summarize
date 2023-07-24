
from flask import Flask

app = Flask(__name__)

from src.main import request_return

@app.route("/")
def me_api():
    return (request_return(), 400)


