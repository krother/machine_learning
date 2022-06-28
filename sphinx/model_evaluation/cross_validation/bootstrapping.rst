Bootstrapping
=============

If you want to calculate a confidence score for your model (a probability range of the model quality), you have 3 options:

-  For some models (e.g. Linear Regression), a confidence interval can be calculated directly using the *t distribution*
-  Other models (e.g. Logistic Regression, SVMs) provide a method to calculate probabilities for predictions.
-  But for many models, neither of this works (in particular, Random Forests and Neural Networks). With these, we have to use **bootstrapping**.

.. image:: Bootstrap_web.png

.. topic:: The Bootstrap algorithm

   1.  You have training data with *N* points.
   2.  Draw *N* random points with replacement.
   3.  Train your model on the sampled data
   4.  Record the test score
   5.  Repeat 2.-4. *K* times
   6.  Sort all collected scores
   7.  Calculate the confidence interval by interpreting the list of scores as **percentiles**.

The scores should be more or less normally distributed for the bootstrapping to be reliable.

Of course, retraining your model 1000 times is costly.

:download:`confidence_score.py <confidence_score.py>`

.. literalinclude:: confidence_score.py


