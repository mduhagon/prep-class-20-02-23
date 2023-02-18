from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is home / default route and I can change things on the fly?'

@app.route('/hello')
def hello():
    return 'Hello World from Python Flask!'

app.run(host='0.0.0.0', port=5000)