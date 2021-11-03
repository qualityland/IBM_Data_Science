import pandas as pd

df = pd.read_csv('imports-85.csv')

print(df)

# convert 'mpg' to 'L/100km':
df['city-mpg'] = 235 / df['city-mpg']
df.rename(columns = {'city-mpg': 'city-L/100km'}, inplace = True)
print(df)
