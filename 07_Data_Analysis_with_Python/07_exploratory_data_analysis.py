import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('imports-85.csv')
df.replace('?', np.nan, inplace=True)
df['price'] = df['price'].astype('float')

# basic statistics for all numerical variables
# mean, std, min, 25%, 50%, 75%, max
df.describe()


# counts for categorical variables
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels':'value_counts'}, inplace=True)
print(drive_wheels_counts)

# box plots
sns.boxplot(x = 'drive-wheels', y = 'price', data = df)

# scatter plots
x = df['engine-size']
y = df['price']
plt.scatter(x, y)
plt.title('Scatterplot of Engine Sizw vs Price')
plt.xlabel('Engine Size')
plt.ylabel('Price')


# grouping
df_test = df[['drive-wheels', 'body-style', 'price']]
df_grp = df_test.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
df_grp
# pivot table
df_pivot = df_grp.pivot(index = 'drive-wheels', columns = 'body-style')
df_pivot

# heatmap
plt.pcolor(df_pivot, cmap = 'RdBu')
plt.colorbar()
plt.show()

# correlation
# price dependent on engine size
sns.regplot(x = 'engine-size', y = 'price', data = df)
plt.ylim(0,)
plt.show()
# price dependent on fuel efficiency
sns.regplot(x = 'highway-mpg', y = 'price', data = df)
plt.ylim(0,)
plt.show()
# price dependent on peak rpm
sns.regplot(x = 'peak-rpm', y = 'price', data = df)
plt.ylim(0,)
plt.show()

# pearson correlation
pearson_coef, p_value = stats.pearsonr(df['horesepower'], df['price'])
print('Pearson correlation:', pearson_coef)
print('P-value:', p_value)

# chi square test (association of categorical variables)
stats.chi2_contingency(cont_table, correction = True)
