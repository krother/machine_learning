
from sklearn.svm import SVC
from sklearn.datasets import make_moons
import numpy as np
from matplotlib import pyplot as plt

X, y = make_moons(500, noise=0.2, random_state=42)

# train a classifier
m = SVC(kernel='rbf', C=0.1)
m.fit(X, y)
print(m.score(X, y))

# plot the decision boundary
N = 200
coord = np.linspace(-1.5, 2.5, N)
xx, yy = np.meshgrid(coord, coord)

Xpred = np.array(list(zip(xx.reshape(N ** 2), yy.reshape(N ** 2))))
ypred = m.predict(Xpred)

Z = ypred.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.seismic)

# plot the data points
colors = np.array(['black', 'white'])
plt.scatter(X[:, 0], X[:, 1], color=colors[y])

plt.show()
