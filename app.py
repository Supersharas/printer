
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def start():
	return "Hello Printing"


app.run(host='127.0.0.1', port=5000)
