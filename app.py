
import json

from flask import Flask
from flask import render_template, request

from book import writer, reader, search

app = Flask(__name__)

@app.route('/')
def start():
	record = reader()
	#record.reverse()
	return render_template("print.html", record=record)


@app.post('/go')
def go():
	content = json.loads(request.data)
	name = content.get('name', None)
	reference = content.get('reference', None)
	cheque_no = content.get('chequeNo', None)
	amount = content.get('amount', None)
	if writer(name, reference, cheque_no, amount):
		return json.dumps({'success': True})
	else:
		print(writer(name, reference, cheque_no, amount))
		return json.dumps({'success': False})

@app.route('/cheque/<name>/<ref>/<nom>/<amount>')
def checque_full(name=None, ref=None, nom=None, amount=None, dat=None):
	print('nm,ref', name, ref)
	return render_template('checque.html', name=ref)
	

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5000)
