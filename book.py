

import os.path
import pandas as pd
from openpyxl import load_workbook
from datetime import datetime

def writer(name, reference, cheque_no, amount):
	day = datetime.now()
	try:
		if os.path.exists("history.xlsx"):
			print("file exists", name)
			df = pd.DataFrame({'Name': [name],
									 'Reference': [reference],
									 'Cheque  Number': [cheque_no],
									 'Amount': [amount],
									 'Date': day.strftime("%m/%d/%Y")})
			#writer = pd.ExcelWriter('history.xlsx', engine='openpyxl')
			reader = pd.read_excel('history.xlsx')
			writer = pd.ExcelWriter('history.xlsx', engine='openpyxl',mode='a', if_sheet_exists='overlay')
			writer.book = load_workbook('history.xlsx')
			writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
			#df.to_excel(writer, sheet_name='Working', index=False)
			df.to_excel(writer,sheet_name='Working',index=False,header=False,startrow=len(reader)+1)
			writer.close()
		else:
			print('inisialising')
			df = pd.DataFrame({'Name': [name],
									 'Reference': [reference],
									 'Cheque  Number': [cheque_no],
									 'Amount': [amount],
									 'Date': day.strftime("%m/%d/%Y")})
			writer = pd.ExcelWriter("history.xlsx", engine='xlsxwriter')
			df.to_excel(writer, sheet_name='Working', index=False)
			writer.save()
		return True
	except Exception as e:
		return False

def reader():
	try:
		dfr = pd.read_excel('history.xlsx')
		#return dfr.to_dict('list')
		#return dfr.to_html()	 
		print(dfr.values.tolist())
		return dfr.values.tolist()
	except:
		return False
		