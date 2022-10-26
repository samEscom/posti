from flask import Flask
from posti_core.posti import Posti
import json


app = Flask(__name__)


@app.route("/")
def home():
    posti = Posti()

    with open("example.json", encoding='utf-8') as f:
        data_file = f.read()
        f.close()

    data = json.loads(data_file)

    res = posti.call_request(
        data.get("method"),
        data.get("url"),
        data.get("params"),
        data.get("json"),
        data.get("headers")
    )
    return str(res)
