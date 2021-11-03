import pandas as pd

df = pd.read_csv('imports-85.csv')
print(df.dtypes)
print(df.descri
be(include = 'all'))
print(df.info())
