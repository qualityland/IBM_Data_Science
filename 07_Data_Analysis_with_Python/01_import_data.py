import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

header_names = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',
'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base',
'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders',
'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio',
'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']

df = pd.read_csv(url, header = None)

df.columns = header_names

df.to_csv('imports-85.csv', index=False)
