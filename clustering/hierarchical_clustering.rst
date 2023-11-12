Hierarchical Clustering
=======================

In hierarchical (or agglomerative) clustering, all data points
start as their own cluster.
They are connected one by one into tree structures
until 

Pseudocode
----------

Here is a generic hierarchical clustering algorithm:

::

    1. create a list of leaf nodes E from all elements you want to cluster
    2. find the pair of distinct elements (e1, e2) in E with the largest similarity
    3. create a new internal node that contains e1 and e2
    4. add the new node to E
    5. remove e1 and e2 from E
    6. repeat from step 2. until there is only one node in E


Drawing the tree
----------------

Here is starting code for an implementation of a tree:

.. literalinclude:: tree.py


Caveats
-------

There exist many variations of the hierarchical clustering idea.
You can see the **distance metric** and **linkage rule** as hyperparameters.

In hieararchical clustering, you can decide *after* the clustering,
how many clusters you want to have.
To get **k** clusters, you would remove the **k** connections 
that were added last.
