from flask import Flask, request, jsonify
import datetime
import pickle
import numpy as np

with open('pickle/model.pkl', 'rb') as pkl_file: 
    model = pickle.load(pkl_file)

app = Flask(__name__)

@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'hello, {name}!'

@app.route('/')
def index():
    return 'Test message. The server is running'

@app.route('/time')
def current_time():
    now = datetime.datetime.now()
    return {'time': now}

@app.route('/add', methods=['POST'])
def add():
    num = request.json.get('num')
    if num > 10:
        return 'too much', 400
    return jsonify({
        'result': num + 1
    })

@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json).reshape(1, 4)
    return jsonify({'prediction': model.predict(features)[0]})

if __name__ == '__main__':
    app.run('localhost', 5000)