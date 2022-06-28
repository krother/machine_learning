
from sklearn.decomposition import PCA

# Average needs to be zero for PCA to work
mean = X.mean()
demeaned = X - mean

pca = PCA(n_components=1)
pca.fit(demeaned)

print(pca.components_)
print(pca.explained_variance_ratio_)
