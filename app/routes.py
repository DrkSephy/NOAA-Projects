from flask import Flask, render_template, request
from flask.ext.cors import CORS
import requests

app = Flask(__name__)
CORS(app, resources=r'/*', headers='Content-Type')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/coordinates')
def getCoordinates():
    print "Pos x: " + request.args.get('pos_x')
    print "Pos y: " + request.args.get('pos_y')
    url = requests.get('http://placekitten.com/' + request.args.get('pos_x') + '/' + request.args.get('pos_y'))
    print url

    return "Hello"
    

if __name__ == '__main__':
    app.run(debug=True)

