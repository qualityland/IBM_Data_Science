import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns

df = pd.read_csv('imports-85.csv')
df.replace('?', np.nan, inplace=True)
df['price'] = df['price'].astype('float')

# fit the model
lm = LinearRegression()
x = df[['highway-mpg']]
y = df[['price']]

lm.fit(x, y)
yHat = lm.predict(x)
print(yHat)

print('Intercept(b0):', lm.intercept_)
print('Coeficient(b1):', lm.coef_)

# regression plot
sns.regplot(x = 'highway-mpg', y = 'price', data = df)
plt.ylim(0,)

# residual plot
sns.residplot(x = 'highway-mpg', y = 'price', data = df)

# distribution plots
ax1 = sns.distplot(df['price'], hist=False, color='r', label='Actual Values')
sns.distplot(yHat, hist=False, color='b', label='Fitted Values', ax=ax1)

# r squared
lm.fit(x, y)
lm.score(x, y)
