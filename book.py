

import os.path
import pandas as pd
from openpyxl import load_workbook
from datetime import datetime

day = datetime.now()
test_day = datetime(2022, 6, 12)
month = test_day.strftime("%B_%Y")

#month = day.strftime("%B_%Y")

def writer(name, reference, cheque_no, amount):
	print('writer activated')
	try:
		if os.path.exists("history.xlsx"):
			check = load_workbook('history.xlsx')
			print("file exists", name)
			df = pd.DataFrame({'Name': [name],
									 'Reference': [reference],
									 'Cheque  Number': [cheque_no],
									 'Amount': [amount],
									 #'Date': day.strftime("%d/%m/%Y")})
									 'Date': test_day.strftime("%d/%m/%Y")})
			#writer = pd.ExcelWriter('history.xlsx', engine='openpyxl')
			if month in check.sheetnames:
				print("sheet_exists", month)
				reader = pd.read_excel('history.xlsx', sheet_name=month)
				writer = pd.ExcelWriter('history.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay')
				writer.book = check			
				writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
				#df.to_excel(writer, sheet_name='Working', index=False)
				df.to_excel(writer,sheet_name=month,index=False,header=False,startrow=len(reader)+1)
			else:
				#append_df_to_excel('t.xlsx', df, sheet_name="Sheet3", startcol=0, startrow=20)
				writer = pd.ExcelWriter("history.xlsx", engine='openpyxl', mode='a', if_sheet_exists='overlay')
				writer.book = check	
				df.to_excel(writer, sheet_name=month, index=False)
			writer.close()
			return True
		else:
			print('inisialising')
			df = pd.DataFrame({'Name': [name],
									 'Reference': [reference],
									 'Cheque  Number': [cheque_no],
									 'Amount': [amount],
									 'Date': day.strftime("%d/%m/%Y")})
			writer = pd.ExcelWriter("history.xlsx", engine='xlsxwriter')
			df.to_excel(writer, sheet_name=month, index=False)
			writer.save()
			return True
	except Exception as e:
		print('exception', e)
		return e

def reader():
	try:
		if day.month == 1:
			prew_month = datetime(day.year, 12, day.day).strftime("%B_%Y")
		else:
			prew_month = datetime(day.year, day.month - 1, day.day).strftime("%B_%Y")
		print("reader activated")
		dfr = pd.read_excel('history.xlsx', sheet_name=month)
		dfr2 = pd.read_excel('history.xlsx', sheet_name=prew_month)
		print('dfr2', dfr2)
		prew = dfr2.values.tolist()
		prew.sort(key=lambda row: datetime.strptime(row[4], "%d/%m/%Y"))
		print('dfr2_next', prew)
		return dfr.values.tolist()
	except:
		return False
		

# local test

#writer("name", "reference", "cheque_no", "amount")

print(reader())