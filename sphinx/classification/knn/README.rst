
k-Nearest-Neighbors
===================

**k-NN is a straightforward prediction method that has no parameters. 
Predictions are made directly from the data. 
Because k-NN is different from most other models, it is useful to include as a baseline model.**

The Algorithm
-------------

.. highlights::

   **To make a prediction for a new data point:**

   1. Calculate the distance of the new data point to all training data points
   2. Identify the *k* closest ones by a distance metric
   3. Calculate the most frequent target value (classification) or their average (regression)
   4. Output the result of 3 as a prediction


Distance Metrics
----------------

The performance of k-NN strongly depends on the choice of the distance metric.
Here are some options:

* Euclidean Distance (default)
* Manhattan Distance
* Cosine Similarity
* Minkowski Distance

k-NN in scikit-learn
--------------------

.. code:: python3

   from sklearn.neighbors import KNeighborsClassifier
   
   m = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
   m.fit(...)


There is also a `KNeighborsRegressor`.


Pros and Cons
-------------

=================== ==============================
Pros                Cons
=================== ==============================
easy to understand  slow, O(N) for each prediction
easy to explain
good baseline
=================== ==============================



.. container:: banner reading

   Further Reading

.. highlights::

   `k-NN Infographic by Avik Jain <https://github.com/Avik-Jain/100-Days-Of-ML-Code/blob/master/Info-graphs/Day%207.jpg>`__

