from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/v1.0/cluster', methods=['GET'])
def index():
    return 'OK!'


app.run(debug=True)
