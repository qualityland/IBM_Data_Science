import pandas as pd

df = pd.read_csv('imports-85.csv')

df['price'] = df['price'].astype('int')

print(df['price'])
