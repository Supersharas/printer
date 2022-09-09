

import os.path
import pandas as pd
from openpyxl import load_workbook
from datetime import datetime

day = datetime.now()
test_day = datetime(2022, 6, 12)
month = day.strftime("%B_%Y")

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
									 'Date': day.strftime("%d/%m/%Y")})
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
		record = {}
		if day.month == 1:
			prew_month = datetime(day.year, 12, day.day).strftime("%B_%Y")
		else:
			prew_month = datetime(day.year, day.month - 1, day.day).strftime("%B_%Y")
		print("reader activated")
		print("month & prew_month", month, prew_month)
		# Only to test if sheet exists
		check = load_workbook('history.xlsx')
		if month in check.sheetnames:
			dfr = pd.read_excel('history.xlsx', sheet_name=month)
			temp = dfr.values.tolist()
			temp.sort(key=lambda row: datetime.strptime(row[4], "%d/%m/%Y"), reverse=True)
			record['month'] = temp
			record['last_num'] = int(temp[0][2]) + 1
		if prew_month in check.sheetnames:		
			dfr2 = pd.read_excel('history.xlsx', sheet_name=prew_month)
			temp2 = dfr2.values.tolist()
			temp2.sort(key=lambda row: datetime.strptime(row[4], "%d/%m/%Y"), reverse=True)
			if 'last_num' not in record:
				record['last_num'] = int(temp2[0][2]) + 1
			record['prew_month'] = temp2
		return record
	except Exception as e:
		print('errpr', e)
		return None

def search(checque_num):
	start = datetime.now().timestamp()
	try:
		dfr = pd.read_excel('history.xlsx', sheet_name=None)
		for key in dfr:
			out = dfr[key].loc[dfr[key]['Cheque  Number'] == checque_num].values.tolist()
			#print('test', dfr.iloc[np.where(dfr.A.values=='foo')])
			if out:
				finish = datetime.now().timestamp()
				print('time taken', finish - start)
				return out[0]
		finish = datetime.now().timestamp()
		print('time taken', finish - start)
		return False
	except Exception as e:
		print('errpr', e)


def stringify(n):
	if n == 0:
		return('Zero')
	elif n == 1:
		return('One')
	elif n == 2:
		return('Two')
	elif n == 3:
		return('Three')
	elif n == 4:
		return('Four')
	elif n == 5:
		return('Five')
	elif n == 6:
		return('Six')
	elif n == 7:
		return('Seven')
	elif n == 8:
		return('Eight')
	else:
		return('Nine')


def convert(amount):
	amount = float(amount)
	amount = int(amount)
	words = {}
	words['ten_mil'] = stringify(amount // 10000000)
	amount = amount % 10000000
	words['mill'] = stringify(amount // 1000000)
	amount = amount % 1000000
	words['hun'] = stringify(amount // 100000)
	amount = amount % 100000
	words['ten'] = stringify(amount // 10000)
	words['thousands'] = stringify(amount // 1000)
	amount = amount % 1000
	words['hundreds'] = stringify(amount // 100)
	amount = amount % 100
	words['tens'] = stringify(amount // 10)
	words['ones'] = stringify(amount % 10)
	return words
		

# local test

#writer("name", "reference", "cheque_no", "amount")

#print(reader())
#print(search('989'))
#print(type(search('989')))