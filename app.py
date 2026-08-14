from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from http import HTTPStatus
from logging.config import dictConfig

from app.services import Services

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
services = Services()
@app.route('/')
def hello_world():
    print("hello world")

@app.route("/puzzle", methods=["POST"])
def puzzle():
    data = request.get_json()
    app.logger.info(f"/puzzle - got request: {data}")
    req_let = data["req"]
    let1 = data["let1"]
    let2 = data["let2"]
    let3 = data["let3"]
    let4 = data["let4"]
    let5 = data["let5"]
    let6 = data["let6"]

    required_let = req_let
    letters = {req_let, let1, let2, let3, let4, let5, let6}
    solutions = services.get_solutions(services.create_puzzle(required_let, letters))
    return jsonify(solutions)
@app.route("/history", methods=["GET"])
def get_history():
    try:
        hist = services.load_puzzle_history()
        data = [
            {
                "letters": puzz.letters,
                "required_letter": puzz.required_let,
                "date": puzz.date
            }
        for puzz in hist
        ]
        return jsonify(data), HTTPStatus.OK
    except Exception as e:
        return jsonify({
            "error": f"Failed to get puzzle history: {e}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == "__main__":
    app.run(host="0.0.0.0")