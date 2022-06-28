
Regularization
==============

.. container:: banner warmup

   What is wrong with this model?

.. highlights::

   .. figure:: overfit.png


Definition
----------

**Regularization** is a set of techniques that constrain the complexity of models.
They thus reduce the risk of **overfitting** and improve the ability of a model to **generalize**.

Overview of regularization methods
----------------------------------

============================================ =======================================
method                                       description
============================================ =======================================
Ridge Regression (L2)                        penalizes the square of coefficients
Lasso (L1)                                   penalizes the absolute coefficients
ElasticNet (L1 + L2)                         weighted combination of Ridge and Lasso
:py:class:`sklearn.linear_model.Ridge`       linear regressor using L2
:py:class:`sklearn.linear_model.Lasso`       linear regressor using L1
:py:class:`sklearn.linear_model.ElasticNet`  linear regressor using L1 + L2
============================================ =======================================

The Bias-variance tradeoff
--------------------------

.. highlights::

   .. figure:: bias_variance_tradeoff.svg

   **Bias** is the expected error created by a model to approximate a real-world relationship.

   **Variance** is the amount by which our model would change with a different training dataset. It is the "flexibility" of our model, balanced against the bias.


Ridge Regression
----------------

**Ridge Regression** penalizes the **coefficients** of linear models.
The penalty is proportional to the square of the parameter value. This
leads to parameters with smaller absolute values.

.. math::

   MSE + \alpha \sum_j^p{\hat{w_j}^2}

The hyperparameter *alpha* controls how strong the regularization is
(low alpha = little regularization, high alpha = very strong
regularization).

The penalty is also called **L2-Norm (Euclidean Norm)**, because it can be written as:

.. math::

   \left||L2 |\right| = \sqrt{x_1^2 + x_2^2 + x_3^2 }

.. warning::

   For L1 or L2 norms to work, the data must be scaled!


.. code:: python3

   from sklearn.linear_model import Ridge

   m = Ridge(alpha=1.0)

.. hint::

   **Ridge Regression** is the first type of regularization you should try.


Lasso Regression
----------------

**Lasso** penalizes the abslute values of coefficients.
It uses the L1 norm (Manhattan Norm).
This pushes some coefficients down to zero.

.. math::

   \left||L1 |\right| = \alpha \sum_j^p{|w_j|}

The hyperparameter **alpha** is the regularization strength.
The higher it is, the more coefficients will become zero.

Therefore, Lasso can be used for **Automatic Feature Selection**.


.. code:: python3

   from sklearn.linear_model import Lasso

   m = Lasso(alpha=1.0)


Elastic Net
-----------

**Elastic Net** combines Ridge and Lasso. The additional hyperparameter
*rho* determines the proportion between both types.

.. math::

   MSE + \alpha \rho \left||w |\right|_1 + \frac{\alpha(1-\rho)}{2}\left||w |\right|_2^2


.. code:: python3

   from sklearn.linear_model import ElasticNet

   m = ElasticNet(alpha=1.0, l1_ratio=0.5)


Feature Selection
-----------------

If you have many features, not all might be required for an accurate model.
To reduce overfitting or simply speed up your model, use **feature selection**

Here are a few approaches to select features:

Remove highly correlated variables
++++++++++++++++++++++++++++++++++

Calculate and plot correlation coefficients:

.. code:: python3

   sns.heatmatp(df.corr(), annot=True)

Then remove those with highly correlated features.
Correlation does not tell everything about the patterns in the data, so this method is not very accurate.

Select significant features
+++++++++++++++++++++++++++

Train a Linear Regression model with ``statsmodels``
and remove features with high p-values.
This method requires that all assumptions for **statistical inference** are met (see :ref:`linreg_assumptions`).

Principal Component Analysis
++++++++++++++++++++++++++++

This key method is covered in :ref:`pca` .

Use Feature Importance in a RandomForest
++++++++++++++++++++++++++++++++++++++++

Train a Random Forest Regressor and examine the ``feature_importance``
values in the trained model.

This method is easy to use and there are few disadvantages (because the RF model does not claim to provide any explanatory power that you could lose).

Recursive Feature Elimination
+++++++++++++++++++++++++++++

RFE is n automated method that trains the model multiple times, eliminating different features in each run.
In scikit the RFE class can be used to optimize an existing model:

.. code:: python3

   from sklearn.feature_selection import RFE

   rfe = RFE(model)
   rfe.fit(X, y)

   rfe.support_  # booleans indicating features to include
   rfe.ranking_  # integers indicating importance

This method is easy to automate if you are happy with a black-box model.

.. container:: banner reading

   Further Reading

.. highlights::

   `Regularized models in scikit-learn <https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification>`__

   Also see this **PyData talk on feature selection strategies**:

   .. youtube:: JsArBz46_3s
