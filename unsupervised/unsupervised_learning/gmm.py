
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.mixture import GaussianMixture


X, _ = make_moons(1000, noise=0.2)
outliers = np.random.normal(0.0, 1.0, (10, 2))

x = np.concatenate([X, outliers])


NCOMP = 3

gmm = GaussianMixture(n_components=NCOMP)
gmm.fit(x)

N = 100
coord = np.linspace(-1.5, 2.5, N)
xx, yy = np.meshgrid(coord, coord)
zz = np.array([xx.ravel(), yy.ravel()]).T

p = gmm.predict_proba(zz)


plt.figure(figsize=(15, 4))
for icomp in range(NCOMP):
    plt.subplot(1, NCOMP, icomp+1)
    comp = p[:, icomp].reshape(xx.shape)
    plt.contourf(xx, yy, comp, alpha=0.75, cmap=plt.cm.seismic)
    plt.scatter(x[:, 0], x[:, 1], color='white', s=3)


plt.figure()
from matplotlib.colors import LogNorm

z = -gmm.score_samples(zz)
z = z.reshape(xx.shape)

CS = plt.contour(xx, yy, z, norm=LogNorm(vmin=1.0, vmax=100.0),
                 levels=np.logspace(0, 3, 10))
CB = plt.colorbar(CS, shrink=0.8, extend='both')
plt.scatter(x[:, 0], x[:, 1], .8)

plt.title('Negative log-likelihood predicted by a GMM')

plt.show()
