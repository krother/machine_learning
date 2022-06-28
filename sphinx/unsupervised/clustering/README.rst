Clustering
==========

.. container:: banner warmup

   Count the Clusters

.. highlights::

   How many clusters do you see in the picture?

   .. figure:: cluster_warmup.png

Key Concepts
------------

======================== ===========================================================
concept                  description
======================== ===========================================================
k-Means Clustering       algorithm assigning spherical clusters
hierarchical Clustering  agglomerative cluster algorithms (building trees)
DBSCAN                   clustering algorithm that takes outliers into account
Curse of Dimensionality  euclidean distance does not work well for higher dimensions
Silhouette Score         metric assessing the spherical shape of clusters
ARI                      metric comparing a clustering to a "gold standard"
======================== ===========================================================

What is clustering used for?
----------------------------

-  Inventory categorization
-  Behavioral segmentation (e.g. by purchase history, activities on application, website, or platform)
-  Define personas based on interests
-  Create profiles based on activity monitoring
-  Detect activity types in motion sensors
-  Group images
-  Separate audio
-  Identify groups in health monitoring
-  Detecting bots
-  Anomaly or outlier detection

K-Means Clustering
------------------

The K-means clustering assigns data points to a predefined number of clusters ``K``.

The algorithms starts with initial estimates for the Κ cluster centers (centroids).
The centers can either be randomly generated or randomly selected from the data set.

Assignment to clusters uses the Euclidean distance:

.. math:: \underset{c_i  \in  C}{\mathbf{argmin}} \ \ dist\left(c_i, x \right)^2

The algorithm iteratively refines the centers until it converges:

.. highlights::

   1. assign each data point to the closest cluster center
   2. calculate new cluster centers as the mean of all datpoints assigned to a cluster
   3. repeat both steps until nothing changes or a stop condition is met

Agglomerative Clustering
------------------------

In Agglomerative Clustering (or hierarchical clustering), all data points start as their own cluster.
A generic agglomerative algorithm looks like this:

.. highlights::

   1. place all data points in a list of nodes
   2. find the two closest nodes
   3. create a connection between them
   4. insert a new node between the two nodes found (e.g. at their mean)
   5. remove the two connected nodes from the list
   6. repeat from 2. until there is only one node left

There exist many variations of this algorithmic idea.
The result of agglomerative clustering can be interpreted (or drawn) as a tree.

Because of that, you can decide *after* the clustering, how many clusters you want to have.
To get ``k`` clusters, you would remove the ``k`` connections that were added last.

DBSCAN
------

DBSCAN looks for groups of data points that are densely packed.
It makes no assumptions about the number of clusters.

Instead, you define two hyperparameters:

-  the minimum number of points per cluster
-  a cutoff distance

The DBSCAN algorithm determines the clusters from that.
Each data point with at least the minimum number of points within the cutoff distance
is assigned to the same cluster as the nearby points.

Thus, the two hyperparameters control the number of clusters indirectly.

Data points that do not have sufficient neighbors, are marked as **outliers**,
as shown by this code example:

.. literalinclude:: outlier_dbscan.py

.. hint::

   DBSCAN can be used for outlier detection!


.. container:: banner challenge1

   Clustering in Scikit

.. highlights::

   Compare the K-Means and DBScan algorithms on the moons dataset using the script below.

   1. Run the script
   2. Exchange `moons` for `blobs`
   3. Adjust the parameters `n_clusters` and `eps` to improve the clustering

   .. literalinclude:: clustering.py


.. container:: banner reading

   Links

.. highlights::

   -  `Clustering methods comparison in scikit-learn <http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html>`__
   -  `Top 5 Clustering Algorithms <https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68>`__

.. container:: banner recap

   Recap Questions

.. highlights::

   -  What are the strengths and weaknesses of K-Means, hierarchical clustering and DBScan?
   -  How can you evaluate a clustering?
   -  What is the curse of dimensionality?
