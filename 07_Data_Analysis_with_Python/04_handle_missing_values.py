import numpy as np
import pandas as pd

df = pd.read_csv('imports-85.csv')

# Drop missing values:
# a) drop the whole observation (row)
new_df = df.dropna(subset = ['price'], axis = 0)
print(new_df)
#df.dropna(subset = ['price'], axis = 0, inplace = True)

# b) drop only the missing value (cell)
new_df = df.dropna(axis=1)
print(new_df)


# Replace missing values
# a) with a mean value
mean = df['normalized-losses'].mean()
new_df = df['normalized-losses'].replace(np.nan, mean)
print(new_df)
