
.. _hyperparam_search:

Hyperparameter Optimization
===========================

**Hyperparameter Optimization** is about finding the
hyperparameters that produce the best model.

.. container:: banner warmup

   Warmup Question

.. highlights::

   Enumerate all model hyperparameters you know.

Key Concepts
------------

===================== ========================================================================================================
concept               description
===================== ========================================================================================================
model parameter       learned through the training algorithm, i.e. ``model.fit()``
hyperparameter        set before the training starts
Grid Search           try every possible combination of hyperparameters and use the combination that produces the best score
Random Search         try randomly sampled hyperparameters. More efficient when searching a larger hyperparameter space
model selection       another word for *hyperparameter search*
===================== ========================================================================================================

Grid Search in Scikit
---------------------

.. literalinclude:: ex_grid_search.py



Pipelines
---------

**Scikit-learn Pipelines** bundle multiple modeling/preprocessing steps into one,
so that you can use them in cross-validation or hyperparameter search.

.. literalinclude:: example_pipeline.py
   :language: python


Feature Engineering in Pipelines
--------------------------------

Many Feature Engineering methods have settings that may be treated as hyperparameters of a pipeline.

To tune them as part of a Grid Search, do the following:

1. Define a dictionary that contains the parameters you want to optimize.
2. Specify the names of hyperparameters in the format `stepname__hyperparametername`
3. Initialize the ``GridSearchCV``.
4. Fit it on your complete training data.
5. Inspect the result with ``pd.DataFrame(grid.cv_results_)``.
6. Have a look at the columns ``'mean_test_score'``, ``'mean_train_score'`` and ``'params'``. Plot the training and cross valdation test score.

You can also get a list of possible parameters by calling ``model_pipe.get_params().keys()``.


.. container:: banner recap

   Recap Questions

.. highlights::

   -  What is the difference between a model parameter and a hyperparameter?
   -  Are feature engineering methods also hyperparameters?
   -  Why shouldn't you tune hyperparameters using the test set?
   -  What is information leakage and why should it be avoided?
   -  Can we try all hyperparameters and feature engineerings to find the best one?
   -  What is the *"no free lunch"* theorem?
