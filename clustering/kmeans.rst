K-Means Clustering
==================

The K-means clustering assigns data points to a predefined number of clusters ``K``.

The algorithms starts with initial estimates for the Κ cluster centers (centroids).
The centers can either be randomly generated or randomly selected from the data set.

Assignment to clusters uses the Euclidean distance:

.. math:: \underset{c_i  \in  C}{\mathbf{argmin}} \ \ dist\left(c_i, x \right)^2

The algorithm iteratively refines the centers until it converges:

::

   1. assign each data point to the closest cluster center
   2. calculate new cluster centers as the mean of all datpoints assigned to a cluster
   3. repeat both steps until nothing changes or a stop condition is met


K-Means from scratch
--------------------

Implement the **k-means clustering** algorithm from scratch.

Step 1
++++++

Generate data for 200 points with two features x1 and x2:

.. code:: python3

   from sklearn.datasets import make_blobs
   
   X, _ = make_blobs(
      n_features=2,
      n_samples=200,
      centers=2,
      random_state=42
      )

Visualize the points as a scatterplot.
We want to group these points by proximity.

Step 2
++++++

Assign the points randomly to two clusters **red** and **blue** e.g. with:

.. code:: python3

   clusters = ["red", "blue"] * 100

Step 3
++++++

Calculate the mean for both x1 and x2.

Step 4
++++++

Calculate the mean x1/x2 for blue and red points separately. We will
call these mean points ``blue_center`` and ``red_center``.

Step 5
++++++

Calculate the euclidean distance from each point to ``blue_center``
and ``red_center``.

Step 6
++++++

Re-label the points. Those points closer to ``blue_center`` shall be
labeled ``blue``, those closer to ``red_center`` shall be labeled
``red``.

Step 7
++++++

Repeat steps 2-4 three times.

Step 8
++++++

The final assignment of the labels ``blue`` and ``red`` is the
k-means clustering.

Draw another scatterplot, using these colors.
