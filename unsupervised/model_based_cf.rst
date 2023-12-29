
.. _model_based_cf:

Matrix Factorization
====================

*Collaborative filtering (CF)* is an umbrella term for various methods related to **recommender systems**.
Despite their differences, all methods in CF use implicit or explicit ratings as input for creating recommendations.
The central assumption is that if two users have rated some items similarly or showed similar behavior in the past,
they will also act similar on future, possibly unseen, items. 

**Non-negative matrix factorization** is another unsupervised learning algorithm that 
aims to extract useful features, by decomposing data to find latent factors which 
can be described by matrices. Although it is classified as an unsupervised learning technique, 
this statistical model can be used to learn and predict ratings.


.. figure:: nmf.png

.. container:: banner warmup

   NMF on Paper

.. highlights::

   Complete the :download:`NMF worksheet <NMF_Exercise.pdf>`.


Key Concepts
------------

================ =======================================================================
concept          description
================ =======================================================================
user-item-matrix a (usually very big) matrix R containing input data
decomposition    R is decomposed into two matrices P and Q
components       the extra dimension of P and Q that defines model complexity
reconstruction   the product of P and Q approximates R
sparsity         most values in the matrix are empty
================ =======================================================================

What is it used for ?
---------------------

-  recommender systems
-  customer segmentation
-  topic modeling (e.g. on a bag of words)
-  dimensionality reduction
-  imputation of missing values

The basic idea
--------------

In a recommendation system like Netflix or MovieLens there is a set of users and a set of items (movies). Each user has rated some items in the system. We want to predict how users would rate items that they have not yet rated, so that we can make recommendations to users.

The information we have on existing ratings can be represented as a matrix. Suppose we have 4 users and 5 movies, and the ratings are integers from 1 to 5, the matrix may look like this:

========== == == == ==
user       u1 u2 u3 u4
========== == == == ==
Titanic    5  3  0  1
Tiffany    4  2  0  1
Terminator 1  1  0  5
Star Trek  1  0  0  4
Star Wars  0  1  5  4
========== == == == ==

We want to describe our ratings *R* by a number of hidden features *K*. Our task is to find two matrices *P* and *Q* such that their product apprioximates R:

.. math::

   \mathbf{R}\approx \mathbf{P}\times \mathbf{Q}^T =\hat{\mathbf{R}}

The intuition behind using matrix factorization to solve this problem is that there should be some latent features (e.g. a mapping of movie genres to user profiles) that determine how a user rates an item.


The math
--------

Our model has the following variables:

======== =====================================
variable description
======== =====================================
U        a set of users
D        a set of items
R        a U x D matrix containing all ratings
K        number of latent features
P        a U x K matrix
Q        a D x K matrix
======== =====================================


Each row of *P* represents the strength of the associations between a user and the features. Similarly, each row of Q represents the strength of the associations between an item and the features.

To get the prediction of a rating of an item *d(j)* by user *u(i)*, we can calculate the dot product of their vectors:

.. math::

   \hat{r}_{ij}=p_i^T \cdot q_j=\sum_{k=1}^K p_{ik} \cdot q_{kj}

Error function
++++++++++++++

Usually there is a difference between the real and the calculated rating matrix:

.. math::

   \mathbf{R} \approx \hat{\mathbf{R}}

This difference called the **error** between the estimated rating and the real rating, can be calculated for each user-item pair:

.. math::

   e^2_{ij}=\left(r_{ij}-\hat{r}_{ij}\right)^2= \left(r_{ij}- \sum_{k=1}^K p_{ik}q_{kj}\right)^2

We consider the squared error because the estimated rating can be either higher or lower than the real rating.

Error gradient
++++++++++++++

To minimize the error, we have to know in which direction we have to modify the values of *p(ik)* and *q(jk)*. In other words, we need to know the gradient at the current values, and therefore we differentiate the above equation with respect to these two variables separately:

.. math::

   \frac{\partial}{\partial p_{ik}} e^2_{ij}= -2\left(r_{ij}-\hat{r}_{ij}\right)(q_{kj})   =-2 e_{ij} q_{kj}

   \frac{\partial}{\partial q_{ik}} e^2_{ij}= -2\left(r_{ij}-\hat{r}_{ij}\right)(p_{ik})   =-2 e_{ij} p_{ik}

Having obtained the gradient, we can now formulate the update rules for both *p(ik)* and *q(kj)*:

.. math::

   p'_{ik}=p_{ik}- \alpha \frac{\partial}{\partial p_{ik}} e^2_{ij}=p_{ik}+ 2\alpha  e_{ij} q_{kj} \\
   q'_{kj}=q_{kj}- \alpha \frac{\partial}{\partial q_{kj}} e^2_{ij}=q_{kj}+ 2 \alpha  e_{ij} p_{ik}

Where *alpha* is the learning rate.

For a given training set *T* we want to minimize our prediction error.

Using our update rule we can set *E* as stop parameter for a given tolerance.

.. math::

   \mathbf{E}=\sum_{u_i,d_j,r_{ij} \in \mathbf{T}}e_{ij}= \sum_{u_i,d_j,r_{ij} \in \mathbf{T}} \left(r_{ij}- \sum_{k=1}^K p_{ik}q_{kj}\right)^2


Regularization
++++++++++++++

We want to introduce a regularization method to avoid overfitting. This can be done by adding a parameter *beta* to the squared error term:

.. math::

   e^2_{ij} = \left(r_{ij}-\hat{r}_{ij}\right)^2 = \left(r_{ij}- \sum_{k=1}^K p_{ik}q_{kj}\right)^2 +\frac{\beta}{2}\sum_{k=1}^K \left(||\mathbf{P}||^2+||\mathbf{Q}||^2\right)

This **regularization term** controls the magnitude of the user-features and item-features such that *P* and *Q* give a good approximation of *R*. So our new update rule could be

.. math::

   p'_{ik}=p_{ik}+ \alpha \frac{\partial}{\partial p_{ik}} e^2_{ij}=p_{ik}+ \alpha\left( 2 e_{ij} q_{kj}-\beta p_{ik}\right)

   q'_{kj}=q_{kj}+ \alpha \frac{\partial}{\partial q_{kj}} e^2_{ij}=q_{kj}+ \alpha\left( 2 e_{ij} p_{ik}-\beta q_{kj}\right)

Adding Biases
+++++++++++++

When the ratings are generated we also have to consider that some users might rate a movie generally higher than very sceptical users. These factors are called **biases**. So every users may have his or her bias *b*.

.. math::

   \hat{r}_{ij}=b+b u_i+ bd_j + \sum_{k=1}^K p_{ik}q_{kj}

where *b* is the gobal bias, *b u(i)* is the bias of user *i* and *bd(j)* is the bias of item *j*.

Plugging this into our model would mean:

.. math::

   b u'_i &= b u_i +\alpha \cdot\left(e_{ij}-\beta bu_i\right)

   b d'_j &= bd_j  +\alpha \cdot\left(e_{ij}-\beta bd_j\right)


the facorization converges faster when biases are applied.

Algorithm
---------

To find the optimal matrices P and Q, the approach is roughly:

.. highlights::

   1. Set the number of components

   2. Set initial values for P and Q (e.g. randomly)

   3. Reconstruct R by multiplying P and Q

   4. Calculate the reconstruction error by comparing with the real data

   5. Calculate the gradient of the reconstruction error

   6. Modify P and Q accordingly

   7. Iterate until P and Q converge

This algorithm is called **Coordinate Descent** and very closely related to gradient descent.


.. container:: banner reading

   Further Reading

.. highlights::

   -  `NMF in scikit-learn <http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html>`__
   -  `Paper: Matrix Factorization for Recommender Systems <https://datajobs.com/data-science-repo/Recommender-Systems-%5BNetflix%5D.pdf>`__
   -  `imputation of missing values with NMF <https://codereview.stackexchange.com/questions/96725/imputing-values-with-non-negative-matrix-factorization>`__
