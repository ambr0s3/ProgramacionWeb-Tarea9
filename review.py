from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/review', methods=['POST','GET'])
def review():
	if request.method == 'GET':
		return "Hello World!"
	if request.method == 'POST':
		
		return jsonify(request.form)

if __name__ == "__main__":
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)