
# coding: utf-8

# 
# 

# # K-Means Clustering

# In[1]:


import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sb  
from scipy.io import loadmat  
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Importing our Data

# In[2]:


data = loadmat('ex7data2.mat') 


# In[3]:


data


# ### This is somewhat an example dataset

# In[4]:


X = data['X']  


# In[5]:


X


# ## We will now set some initial centroids in 2D plane

# In[6]:


initial_centroids = np.array([[3, 3], [6, 2], [8, 5]])


# ## Implementing an algortihm to find the closest centroids

# In[7]:


def find_closest_centroids(X, centroids):  
    m = X.shape[0]
    k = centroids.shape[0]
    idx = np.zeros(m)

    for i in range(m):
        min_dist = 1000000
        for j in range(k):
            dist = np.sum((X[i,:] - centroids[j,:]) ** 2)
            if dist < min_dist:
                min_dist = dist
                idx[i] = j

    return idx


# ### Let's see to which centroids our dataset would have been located to

# In[8]:


find_closest_centroids(X,initial_centroids)[0:3]


# ## We now know that:
# ### The first data poitn fits to the 0. centroid. 
# ### The second data poitn of X fits to the 2. centroid 
# ### and third data point of X fits to the 1. centroid

# In[9]:


idx = find_closest_centroids(X, initial_centroids)  


# In[10]:


idx[0:3]


# In[11]:


idx


# In[12]:


np.where(idx == 2)


# ## As a next step we need a function to compute the new centroids positions.

# In[13]:


def compute_centroids(X, idx, number_of_centroids):  
    m, n = X.shape
    centroids = np.zeros((number_of_centroids, n))

    for i in range(number_of_centroids):
        indices = np.where(idx == i)
        centroids[i,:] = (np.sum(X[indices,:], axis=1) / len(indices[0])).ravel()

    return centroids


# ## The centroid is simply the mean of all of the examples currently assigned to the cluster.

# In[14]:


compute_centroids(X, idx, 3)


# In[15]:


X.shape


# In[16]:


initial_centroids.shape[0]


# In[17]:


initial_centroids


# ## In order to run the algorithm we just need to alternate between assigning examples to the nearest cluster and re-computing the cluster centroids.

# In[18]:


def run_k_means(X, initial_centroids, max_iters):  
    m, n = X.shape
    k = initial_centroids.shape[0]
    idx = np.zeros(m)
    centroids = initial_centroids

    for i in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_centroids(X, idx, k)

    return idx, centroids


# In[19]:


run_k_means(X, initial_centroids, 10) 


# ## Plotting the results

# In[20]:


cluster1 = X[np.where(idx == 0)[0],:]  
cluster2 = X[np.where(idx == 1)[0],:]  
cluster3 = X[np.where(idx == 2)[0],:]

fig, ax = plt.subplots(figsize=(12,8))  
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')  
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')  
ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3')  
ax.legend() 


# ## Assigning the the new values for the plot

# In[21]:


idx,centroids=run_k_means(X, initial_centroids, 10) 


# In[22]:


idx


# In[23]:


X[np.where(idx == 0)[0],:]


# In[24]:


cluster1 = X[np.where(idx == 0)[0],:]  
cluster2 = X[np.where(idx == 1)[0],:]  
cluster3 = X[np.where(idx == 2)[0],:]

fig, ax = plt.subplots(figsize=(12,8))  
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')  
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')  
ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3')  
ax.legend() 


# ## We chose initital centroids.
# ## But there is also a way to choose from the dataset

# In[25]:


def init_centroids(X, number_of_centroids):  
    m, n = X.shape
    centroids = np.zeros((number_of_centroids, n))
    idx = np.random.randint(0, m, number_of_centroids)

    for i in range(number_of_centroids):
        centroids[i,:] = X[idx[i],:]

    return centroids


# In[26]:


init_centroids(X, 7) 


# # Hands on K Means

# In[27]:


df=pd.read_csv("https://raw.githubusercontent.com/datascienceinc/learn-data-science/master/Introduction-to-K-means-Clustering/Data/data_1024.csv",delimiter="\t",index_col=0)


# In[28]:


df.to_csv("truck.csv")


# In[29]:


df=pd.read_csv("truck.csv")


# In[30]:


df.head()


# In[31]:


df.plot.scatter(x="Distance_Feature",y="Speeding_Feature")


# In[27]:


from sklearn.cluster import KMeans


# In[33]:


f1 = df['Distance_Feature'].values
f2 = df['Speeding_Feature'].values


# In[34]:


f2.reshape((4000,-1))


# In[35]:


x=f1.reshape((4000,-1))


# In[36]:


y=f2.reshape((4000,-1))


# In[37]:


X=np.hstack([x,y])


# In[38]:


X


# ## Fitting a model with 2 centroids

# In[39]:


kmeans = KMeans(n_clusters=2).fit(X)


# In[40]:


kmeans.labels_


# In[41]:


ray= kmeans.labels_


# In[42]:


cluster1 = X[np.where(ray == 0)[0],:]  
cluster2 = X[np.where(ray == 1)[0],:]  


fig, ax = plt.subplots(figsize=(12,8))  
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')  
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')  
 
ax.legend() 


# ## Fitting a model with 3 centroids

# In[43]:


kmeans3 = KMeans(n_clusters=3).fit(X)


# In[44]:


ray3=kmeans3.labels_


# In[45]:


ray3


# In[46]:


cluster1 = X[np.where(ray3 == 0)[0],:]  
cluster2 = X[np.where(ray3 == 1)[0],:]
cluster3 = X[np.where(ray3 == 2)[0],:]


fig, ax = plt.subplots(figsize=(12,8))  
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')  
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')  
ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3') 
 
ax.legend() 


# ## Fitting a model with 3 centroids

# In[34]:


kmeans4 = KMeans(n_clusters=4,random_state=10).fit(X)


# In[35]:


ray4=kmeans4.labels_


# In[36]:


cluster1 = X[np.where(ray4 == 0)[0],:]  
cluster2 = X[np.where(ray4 == 1)[0],:]
cluster3 = X[np.where(ray4 == 2)[0],:]
cluster4 = X[np.where(ray4 == 3)[0],:]

fig, ax = plt.subplots(figsize=(12,8))  
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')  
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')  
ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3') 
ax.scatter(cluster4[:,0], cluster4[:,1], s=30, color='y', label='Cluster 4') 
ax.legend()  


# In[5]:


from sklearn.datasets import make_moons


# In[8]:


X,y=make_moons(noise=0.25,random_state=0)


# In[9]:


plt.scatter(X[:,0],X[:,1])


# In[10]:


from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler


# In[11]:


centers = [[1, 1], [-1, -1], [1, -1]]


# In[16]:


X


# In[14]:


X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,random_state=0)


# In[15]:


X=StandardScaler().fit_transform(X)


# In[18]:


db = DBSCAN(eps=0.3, min_samples=10).fit(X)


# In[20]:


db.labels_


# In[22]:


core_samples_mask = np.zeros_like(db.labels_, dtype=bool)


# In[23]:




core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_


# In[24]:


n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))


# In[25]:


unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()


# In[37]:


from __future__ import print_function

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

print(__doc__)

# Generating the sample data from make_blobs
# This particular setting has one distinct cluster and 3 clusters placed close
# together.
X, y = make_blobs(n_samples=500,
                  n_features=2,
                  centers=4,
                  cluster_std=1,
                  center_box=(-10.0, 10.0),
                  shuffle=True,
                  random_state=1)  # For reproducibility

range_n_clusters = [2, 3, 4, 5, 6]

for n_clusters in range_n_clusters:
    # Create a subplot with 1 row and 2 columns
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)

    # The 1st subplot is the silhouette plot
    # The silhouette coefficient can range from -1, 1 but in this example all
    # lie within [-0.1, 1]
    ax1.set_xlim([-0.1, 1])
    # The (n_clusters+1)*10 is for inserting blank space between silhouette
    # plots of individual clusters, to demarcate them clearly.
    ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

    # Initialize the clusterer with n_clusters value and a random generator
    # seed of 10 for reproducibility.
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(X)

    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    silhouette_avg = silhouette_score(X, cluster_labels)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)

    # Compute the silhouette scores for each sample
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    y_lower = 10
    for i in range(n_clusters):
        # Aggregate the silhouette scores for samples belonging to
        # cluster i, and sort them
        ith_cluster_silhouette_values =             sample_silhouette_values[cluster_labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.spectral(float(i) / n_clusters)
        ax1.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)

        # Label the silhouette plots with their cluster numbers at the middle
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples

    ax1.set_title("The silhouette plot for the various clusters.")
    ax1.set_xlabel("The silhouette coefficient values")
    ax1.set_ylabel("Cluster label")

    # The vertical line for average silhouette score of all the values
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

    ax1.set_yticks([])  # Clear the yaxis labels / ticks
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    # 2nd Plot showing the actual clusters formed
    colors = cm.spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter(X[:, 0], X[:, 1], marker='.', s=30, lw=0, alpha=0.7,
                c=colors, edgecolor='k')

    # Labeling the clusters
    centers = clusterer.cluster_centers_
    # Draw white circles at cluster centers
    ax2.scatter(centers[:, 0], centers[:, 1], marker='o',
                c="white", alpha=1, s=200, edgecolor='k')

    for i, c in enumerate(centers):
        ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
                    s=50, edgecolor='k')

    ax2.set_title("The visualization of the clustered data.")
    ax2.set_xlabel("Feature space for the 1st feature")
    ax2.set_ylabel("Feature space for the 2nd feature")

    plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
                  "with n_clusters = %d" % n_clusters),
                 fontsize=14, fontweight='bold')

    plt.show()

