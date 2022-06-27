import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('history.xlsx', sheet_name='Sheet1')

print(df)