from flask import Flask, render_template, request
from posti_core.posti import Posti
import json

app = Flask(__name__)

posti = Posti()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/call", methods=["POST", "GET"])
def call_posti():
    if request.method == "POST":
        data_json = request.get_json()
        res = posti.call_request(
            data_json.get("method"),
            data_json.get("url"),
            data_json.get("params"),
            data_json.get("json"),
            data_json.get("headers")
        )
        return res

    return {
        "message": "no validate"
    }


@app.route("/example")
def example_from_file():
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
    return res


if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0")
    app.run(debug=True)
