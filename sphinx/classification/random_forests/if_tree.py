
import pandas as pd
from sklearn.metrics import accuracy_score

df = pd.read_csv('train.csv', index_col=0)
y = df['Survived']

ypred = []
for i, row in df.iterrows():
    if row[...] == ...:
        ...


print(accuracy_score(y, ypred))
