
from sklearn import cluster, datasets
from sklearn.neighbors import kneighbors_graph
import pylab as plt
import numpy as np

colors = np.array(['red', 'blue', 'green', 'orange', 'black', 'yellow']*100)

# generate data
moons = datasets.make_moons(n_samples=1000, noise=.05)[0]
blobs = datasets.make_blobs(n_samples=1000, random_state=8)[0]

# algorithm 1: KMeans
kmeans = cluster.MiniBatchKMeans(n_clusters=2)
kmeans.fit(moons)
clusters_k = kmeans.predict(moons)

plt.scatter(moons[:, 0], moons[:, 1], s=10, 
            color=colors[clusters_k])
plt.show()

# algorithm 2: DBSCAN
dbscan = cluster.DBSCAN(eps=0.3)
dbscan.fit(moons)
clusters_db = dbscan.labels_.astype(np.int)

plt.scatter(moons[:, 0], moons[:, 1], s=10, 
            color=colors[clusters_db])
plt.show()
