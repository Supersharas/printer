import xlwings
import pandas

with xlwings.App() as App:
    _ = App.books.open('my.xlsx')
    rng = App.books['history.xlsx'].sheets['Sheet1'].tables['Table1'].range
    df: pandas.DataFrame = rng.expand().options(pandas.DataFrame).value


print(df)