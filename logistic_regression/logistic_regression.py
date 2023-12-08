
from sklearn.datasets import make_moons
from sklearn.____ import ____

X, y = make_moons(n_samples=200, noise=0.3)

m = LogisticRegression(C=1e5)
m.____(X, y)

print(m.____(X, y))
