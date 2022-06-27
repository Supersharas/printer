
import json
import os.path
import pandas as pd
import datetime

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def start():
	return render_template("print.html")


@app.post('/go')
def new_song():
  content = json.loads(request.data)
  name = content.get('name', None)
  reference = content.get('reference', None)
  cheque_no = content.get('chequeNo', None)
  amount = content.get('amount', None)
  try:
    if os.path.exists("history.xlsx"):
      print("file exists", name)
    else:
      print('inisialising')
      df = pd.DataFrame({'Name': name,
                   'Reference': reference,
                   'Cheque  Number': cheque_no,
                   'Amount': amount,
                   'Date': datetime.date})
      writer = pd.ExcelWriter("history.xlsx", engine='xlsxwriter')
      df.to_excel(writer, sheet_name='Sheet1', startrow=1, index=False)
      writer.save()
  except Exception as e:
  	return json.dumps({'error': repr(e)})
  dfr = pd.read_excel ('history.xlsx')
  print('reading', dfr)
  return json.dumps({"reading": str(dfr)})

if __name__ == "__main__":
  app.run(host='127.0.0.1', port=5000)
