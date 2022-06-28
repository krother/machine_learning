Similarity Measures
===================


Cosine similarity
~~~~~~~~~~~~~~~~~

As an Euclidean similarity measure, **cosine similarity** is commonly used:

.. math::

   cos(X, Y) = \frac{X \cdot Y}{\left||X |\right| * \left||Y |\right|}

Or, in more detail:

.. math::

   cos(X, Y) = \frac{\sum_i^n{X_i*Y_i}}{\sqrt{\sum_i{X_i^2}}*\sqrt{\sum_i{Y_i^2}}}


Adjusted Cosine Similarity
~~~~~~~~~~~~~~~~~~~~~~~~~~

Simple cosine similarity does not account for different rating scales. There might be *happy raters* who usually give higher ratings 
and *pessimistic raters* who generally give really low ratings.

To account for these differences we can **normalize** the rating data by 
substracting the users' average from each rating:

.. math::

   cos_{adj}(X, Y) = \frac{\sum_i^n{(X_i-\bar{X})*(Y_i-\bar{Y})}}{\sqrt{\sum_i{(X_i-\bar{X})^2}}*\sqrt{\sum_i{(Y_i-\bar{Y})^2}}}

It turns out that (for user-user similarities) this measure is similar to **Pearson's correlation** that we frequently use in statistics. 


Jaccard similarity
~~~~~~~~~~~~~~~~~~
For **binary variables** you might use the **Tanimoto coefficient** (also see **Jaccard Index**). It uses the **number of bits**:

.. math::

   jac(X, Y) = \frac{nbits(X \cap Y)}{nbits(X) * nbits(Y) - nbits(X \cap Y)}

Or in simpler terms:

.. math::

   jac(X, Y) = \frac{\text{#users that liked/bought X and Y}}{\text{#users that liked/bought X or Y}}

