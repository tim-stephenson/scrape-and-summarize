
from flask import Flask

app = Flask(__name__)


@app.route("/")
def me_api():
    return {
        "parameter1": "val1",
        "parameter2": "val2",
        "parameter3": ["val3a", "val3b"],
    }

