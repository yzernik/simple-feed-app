from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/feeds', methods=['GET', 'POST'])
def feeds():
    if request.method == 'GET':
        return 'Get all the feeds here.'
    if request.method == 'POST':
        return 'creating new feed named: ' + request.form['name']

if __name__ == '__main__':
    app.run()
