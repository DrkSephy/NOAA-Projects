from flask import Flask, render_template, request
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*', headers='Content-Type')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/coordinates')
def getCoordinates():
    print "Pos x: " + request.args.get('pos_x')
    print "Pos y: " + request.args.get('pos_y')
    return "Hello"
    

if __name__ == '__main__':
    app.run(debug=True)

