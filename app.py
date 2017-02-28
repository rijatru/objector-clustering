from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'OK!'


app.run(debug=True)
