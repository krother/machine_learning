
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

np.random.seed(40)

N = 40

x = np.hstack([
       np.random.normal(3.0, 1.0, N//2),
       np.random.normal(5.0, 1.0, N//2)])
y = [0] * (N//2) + [1] * (N//2)

m = LogisticRegression(C=1000000.0)
m.fit(x.reshape((N,1)), y)

xm = np.linspace(0.0, 8.0, 200).reshape(-1, 1)
ym = m.predict_proba(xm)[:,1]

plt.plot(x, y, 'bo')
plt.plot(xm, ym, 'r-')
plt.xlabel('x')
plt.ylabel('probability')
plt.savefig('logreg.png')
