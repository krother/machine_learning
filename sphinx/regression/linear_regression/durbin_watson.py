"""
Durbin-Watson-Test

tests for Autocorrelation:

result close to 0 - positive autocorrelation
result close to 4 - negative autocorrelation
result close to 2 - no autocorrelation

"""
import numpy as np
from statsmodels.stats.stattools import durbin_watson
from sklearn.linear_model import LinearRegression

X = np.linspace(0.0, 20.0, 1000).reshape(1000, 1)
y1 = np.sin(X).flatten()
durbin_watson(y1, axis=0)

y2 = np.random.normal(0.0, 1.0, 1000).flatten()
durbin_watson(y2, axis=0)


m = LinearRegression()
m.fit(X, y1)
y1pred = m.predict(X)
resids1 = y1pred - y1

m.fit(X, y2)
y2pred = m.predict(X)
resids2 = y1pred - y2

durbin_watson(resids1, axis=0)
durbin_watson(resids2, axis=0)
