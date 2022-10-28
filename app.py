
import json

from flask import Flask
from flask import render_template, request

from book import writer, reader, search, convert, do_edit

from datetime import datetime
import webbrowser
import re
pattern = re.compile("[0-9\\.]*")

day = datetime.now()

app = Flask(__name__)

@app.route('/')
def start():
	record = reader()
	return render_template("print.html", record=record)

@app.post('/edit')
def edit():
	content = json.loads(request.data)
	cheque_date = content.get('checqueDate', None)
	cheque_no = content.get('chequeNo', None)
	name = content.get('name', None)
	reference = content.get('reference', None)
	amount = content.get('amount', None)
	old_no = content.get('oldNo',None)
	result = do_edit(cheque_date, old_no, name, reference, cheque_no, amount)
	return json.dumps(result)

@app.post('/go')
def go():
	content = json.loads(request.data)
	name = content.get('name', None)
	reference = content.get('reference', None)
	cheque_no = content.get('chequeNo', None)
	print('match', pattern.match(cheque_no))
	if not pattern.fullmatch(cheque_no):
		return json.dumps({'Success': False, 'msg': 'Cheque number not valid!'})
	amount = content.get('amount', None)
	if not pattern.fullmatch(amount):
		return json.dumps({'Success': False, 'msg': 'Amount not valid!'})
	if writer(name, reference, cheque_no, amount):
		return json.dumps({'Success': True})
	else:
		print(writer(name, reference, cheque_no, amount))
		return json.dumps({'Success': False})

@app.route('/cheque/<name>/<ref>/<nom>/<amount>')
def checque_full(name=None, ref=None, nom=None, amount=None):
	
	amount = float(amount[1:])
	return render_template('checque.html', name=name, ref=ref, nom=nom, amount=f"{amount:.2f}",
		dat=day.strftime("%d/%m/%Y"), words = convert(amount))

webbrowser.open('http://127.0.0.1:5000', new=0, autoraise=True)	

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5000)

