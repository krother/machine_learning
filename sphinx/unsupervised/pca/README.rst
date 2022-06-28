Principal Component Analysis
============================

What is PCA?
------------

**Principal Component Analysis (PCA)** is an unsupervised learning method used for dimensionality reduction.

For multivariate data sets, it often happens that a few measured variables already contain a large part of the information and other metrics contribute little. 
**Principal Component Analysis** is procedure that allows to condense such data sets to the *"most informative"* dimensions.

What is Dimensionality Reduction used for?
------------------------------------------

Having fewer features has a couple of advantages:

-  some models only work with fewer features (e.g. clustering or t-SNE)
-  the calculation time of models is shorter
-  the risk of overfitting is less severe
-  PCA gets rid of multicolinearity in Linear Regression
-  it helps you to understand how much information there is in the data

Key Concepts
------------

======================== ================================================
concept                  description
======================== ================================================
dimensionality reduction replacing features by a smaller subset
principal components     new, ranked features the data is transformed to
vanilla PCA              useful if the data fits into memory
incremental PCA          PCA variant that works in batches
                         (for lots of data or frequent updates)
randomized PCA           faster when reducing number of dimensions heavily
Kernel PCA               PCA variant for non-linear transformations
======================== ================================================

How does PCA work?
------------------

PCA transforms the **feature space X** into a **new feature space T** using the **principal components W**:

.. math::

   \mathbf{T} = \mathbf{X} \cdot \mathbf{W}


Each principal component is a linear combination of the original features that explains the **maximum variance** in the data.

The principal components are **ranked**:

- the first principal component always explains the highest proportion of the variance.
- the second principal component explains the next highest proportion and so on.
- the maximum number of principal components is the number of original features.
- the more principal components you use, the more accurate your description of the data becomes.
- if you use the maximum number of principal components, no information is lost during the transformation.
- with fewer principal components than original features, the new feature space is an *approximation* of the original features.

Algorithm
---------

Step 1: Calculate the covariance matrix
+++++++++++++++++++++++++++++++++++++++

It is assumed that the variables that have the greatest variance also contain the most information.

To measure the redundancy in the data, we calculate the covriance of each measured variable with each other. This then results in the **covariance matrix C**:

.. math::

   C_{ij}=\frac{1}{n-1}\sum^n_{k=1}\left(x_{ki}-\bar{x}_i\right)\left(x_{kj}-\bar{x}_j\right)

where *i* and *j* are the features and *n* the number of data points.

.. note::

   The features may have very different value ranges. Before calculating the covariance it is not only advisable to de-mean the data but also scale it.

Step 2: Calculate the eigenvectors
++++++++++++++++++++++++++++++++++

Calculate the eigenvectors of the matrix C and sort them according to their corresponding eigenvalues (largest first). The eigenvectors are the so-called principal components and the associated eigenvalues indicate how much variance ("information") is included in this principal component is included.

The cumulative sum of the first *x* eigenvalues divided by the total sum of eigenvalues gives the percentage of variance that is explained by the first *x* principal components.

Step 3: Transform the data
++++++++++++++++++++++++++

Project the original data set by multiplying it with the desired number of principal components:

.. math::

   \mathbf{T}=\mathbf{X}\cdot \mathbf{W}

where **X** is the (normalized) data set and **W** is a matrix, containing the principal components in columns.


Code Example
------------

.. literalinclude:: ex_pca.py

.. container:: banner debug

   Caveats

.. highlights::

   -  **Your data needs to have a mean of zero.** Otherwise the principal components will simply represent the mean.
   -  You need to set the number of principal components up front
   -  Make sure to check ``m.explained_variance_ratio_`` after fitting.
   -  The principal components are hard to interpret. A feature that is a linear combination of other features does not have an inherent meaning.
   -  The transformed data loses information


.. container:: banner reading

   Links

.. highlights::

   -  `PCA tutorial <https://www.cs.princeton.edu/picasso/mats/PCA-Tutorial-Intuition_jp.pdf>`__
   -  `More on the math behind PCA <http://www.cs.otago.ac.nz/cosc453/student_tutorials/principal_components.pdf>`__

.. container:: banner recap

   Recap Questions

.. highlights::

   - Can you reverse the transformation of a PCA?
   - What are the model parameters of a PCA?
   - What are the hyperparameters of a PCA?
   - Can you use PCA on a highly non-linear dataset?
   - If you use PCA to reduce a 1000-dimensional dataset, how many dimensions will the transformed data have if you want to have an explained variance of 95%?
