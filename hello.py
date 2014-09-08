from flask import Flask 
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/testing')
def test():
    return 'Testing!'

if __name__ == '__main__':
    app.run()