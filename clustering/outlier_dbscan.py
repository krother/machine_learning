
from sklearn.datasets import make_moons
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN

X, _ = make_moons(1000, noise=0.2)
outliers = np.random.normal(0.0, 1.0, (10, 2))

x = np.concatenate([X, outliers])


m = DBSCAN(eps=0.3)
m.fit(x)

c = m.fit_predict(x)

cols = np.array(['blue', 'red'])
c = m.labels_.astype(np.int)

plt.scatter(x[:,0], x[:,1], c=cols[c])
plt.show()
