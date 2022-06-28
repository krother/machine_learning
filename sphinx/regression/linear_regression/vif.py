import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor as VIF
from matplotlib import pyplot as plt


df = pd.read_csv('train.csv', index_col=0, parse_dates=True)
del df['atemp']
df = df.iloc[:, :-3]

vifs = [VIF(df.values, i) for i, colname in enumerate(df)]
s = pd.Series(vifs, index=df.columns)
s.plot.bar()
