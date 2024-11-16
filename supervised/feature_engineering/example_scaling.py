
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(X)

Xtrans = scaler.transform(X)
print("data after:\n", Xtrans[:5])
