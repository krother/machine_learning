DBSCAN
------

The DBSCAN clustering algorithm looks for groups of data points
that are densely packed.
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
