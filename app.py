from flask import Flask, jsonify, request
from werkzeug.exceptions import abort
from clustering import load_data

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/api/v1.0/cluster', methods=['GET'])
def source():

    return load_data()

    #return jsonify({'tasks': tasks})


@app.route('/api/v1.0/cluster', methods=['POST'])
def create_task():

    if not request.json or not request.json['task']:
        abort(400)

    request_task = request.json.get('task')

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request_task.get('title'),
        'description': request_task.get('description', ""),
        'done': False
    }

    tasks.append(task)
    return jsonify({'task': task}), 201


if __name__ == '__main__':
    app.run(debug=True)
