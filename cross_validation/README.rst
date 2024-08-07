
.. _crossval:

Cross-Validation
================

Concepts
--------

=========================================================== ==============================
Function
=========================================================== ==============================
:py:func:`sklearn.model_selection.cross_validate`           k-fold cross-validation
:py:class:`sklearn.model_selection.ShuffleSplit`            Shuffle-split cross-validation
:py:class:`sklearn.model_selection.StratifiedShuffleSplit`  stratified Shuffle-split CV
:py:func:`sklearn.utils.resample`                           Select sample from dataset
=========================================================== ==============================

K-fold Cross-Validation
-----------------------

.. figure:: crossval.png

**K-fold Cross-Validation** divides the dataset into *k* portions called **folds**. 
Each fold serves as a test dataset once, and the rest as a training set.
This results in a table of *k* scores for the training and test fold 
that allow to evaluate the robustness of the model.

With cross validation we can use all our training data for fitting the model as we don't need to
apply an additional train-validation split. On the other side, cross validation is computationally costly, 
especially for large datasets. 

.. code:: python3

   from sklearn.model_selection import cross_validate

   model = LinearRegression()
   cv = cross_validate(model, X_train_trans, y_train, 
                       cv=5,
                       scoring='r2', 
                       return_train_score=True
   )
   # convert the dictionary of lists into a DataFrame
   cv = pd.DataFrame(cv)
   print(cv)


.. container:: banner milestone

   Cross-Validation with the Mean Squared Log Error

.. highlights::

   Try 5-fold cross-validation with `scoring='neg_mean_squared_log_error'` on the Bike dataset.

   How would you interpret the result?



Shuffle-Split
-------------

**Shuffle-Split** is a more flexible alternative, especially with large datasets. It allows you to select random samples with a specific size.
The **stratified** variant takes care to select representative features.

.. container:: banner challenge2

   Cross-Val vs. Shuffle-Split

.. highlights::

   Compare **k-fold CV** and **Shuffle-split CV** on the Titanic dataset.
   What impact does the size of the dataset have?
   What impact does stratification have?


Cross-Validation and Time Series Data
-------------------------------------

In time series, we try to **predict the future from the past**.
Because of that, the test data always has to be *after* the training portion.
In this case, cross-validation should look like this:

.. figure:: tssplit.png

There is no scikit function for that, you need to slice the data folds yourself.


Bootstrapping
-------------

If you want to calculate a confidence score for your model (a probability range of the model quality), you have 3 options:

-  For some models (e.g. Linear Regression), a confidence interval can be calculated directly using the *t distribution*
-  Other models (e.g. Logistic Regression, SVMs) provide a method to calculate probabilities for predictions.
-  But for many models, neither of this works (in particular, Random Forests and Neural Networks). With these, we have to use **bootstrapping**.

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

.. literalinclude:: confidence_score.py



.. container:: banner recap

   Recap Questions

.. highlights::

   -  What is a sampling bias?
   -  What is the purpose of a validation set?
   -  Why is a single validation set not sufficient?
   -  What does it mean if your cross-validation scores fluctuate a lot?
   -  What is stratification?
