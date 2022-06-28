
import numpy as np
import statsmodels.api as sm
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('train.csv', index_col=0, parse_dates=True)
X = df.iloc[:, :9]
y = df['count']

m = LinearRegression()
m.fit(X, y)
ypred = m.predict(X)
resids = ypred - y

# perfect example
a = np.random.normal(5, 5, 250)
pl = sm.qqplot(a, line='r')

# QQ-plot for our residuals --> no homoscedasticity
pl = sm.qqplot(resids, line='r')
