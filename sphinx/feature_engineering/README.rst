
.. _feature_eng_I:

Scaling and Encoding
====================

**Feature Engineering** refers to all techniques that make your data easier for a model to understand.
Here is an (incomplete) list of scaling/encoding techniques:

=================== ======================================================
class               description
=================== ======================================================
OneHotEncoder       converts a category to binary columns
KBinsDiscretizer    bins scalar data to make it categorical
MinMaxScaler        normalize the data to the range 0.0 - 1.0
factorizing         converts categories to a single integers
target encoding     uses proportions of the target class
Log-Transform       converts exponential to linear
=================== ======================================================

**Feature Engineering** means preprocessing your data *before* building a model. 
The goal of Feature Engineering is to derive a *better* representation of your input data. 


.. container:: banner python

   The Transform Pattern

.. highlights::

   In scikit-learn, there is a generic `transform()` mechanism that applies to all feature engineering methods:

   1. create a transformer object
   2. call `.fit()` on the training data
   3. call `.transform()` on the test/validation data

   .. warning::

      **Never call `.fit()` on test/validation data. This ruins everything!**




One-Hot Encoding
----------------

One-Hot encoding (dummy encoding) transforms a categorical variable into binary features.

Every distinct category becomes a binary column, so that every row has exactly one positive value.

======== ======= ===== ===== =====
category -->     thyme chili basil
======== ======= ===== ===== =====
thyme             1     0     0
chili             0     1     0
chili             0     1     0
thyme             1     0     0
basil             0     0     1
======== ======= ===== ===== =====

.. code:: python3

   from sklearn.preprocessing import OneHotEncoder

   one_hot = OneHotEncoder(sparse=False, handle_unknown='ignore')

   one_hot.fit(Xtrain[['column_name']])           # learn the categories
   one_hot.transform(Xtrain[['column_name']])     # apply the transformation


.. warning::

   The last column outputted from the ``OneHotEncoder`` is redundant, because
   the value of the last one-hot encoded column can logically be deduced from the others.
   If you take all columns, your data will be **multicollinear**, which creates trouble with some models.

   You could remove the last column from the transformed data with the parameter ``drop='first'``.
   However, in that case you can't use ``handle_unknown='ignore'`` anymore.


Binning
-------

Binning transforms a continuous, numeric variable to an ordinal, categorical variable,
e.g. all ages --> ['child', 'adolescent', 'middle-aged', 'elderly'].

Each "bin" is its own category.

The ``KBinsDiscretizer`` also one-hot-encodes the resulting categories straight away:

.. code:: python3

   from sklearn.preprocessing import KBinsDiscretizer

   binner = KBinsDiscretizer(n_bins=3, encode='onehot-dense', strategy='quantile')
   binner.fit(Xtrain[['column_name']])
   binner.transform(Xtrain[['column_name']])

The **quantile** strategy will place the same number of data points in each bin.
An alternative, the **uniform** strategy will create bins of equal width.



Scaling
-------

Scaling adjusts the range of the data or the mean and standard deviation to a defined range.

Many models require data to be scaled (e.g. SVM and Neural Networks).
Logistic and Linear Regression are faster if the data is scaled.

**Min-Max Scaling** scales data to values in the range between 0 and 1.

.. math::

   X_i' = \frac{X_i - min(x)}{max(x) - min(x)}

You would use the ``MinMaxScaler`` class on the data *after* transforming the columns:

.. code:: python3

   from sklearn.preprocessing import MinMaxScaler

   scaler = MinMaxScaler()
   scaler.fit(Xtrain[['column_name']])                    # learn the min and max
   scaler.transform(Xtrain[['column_name']])              # apply the transformation


Alternatively, the ``StandardScaler`` scales to a normal distribution with mean 0 and standard deviation 1.
The syntax is the same, only the ``import`` is different:

.. code:: python3

   from sklearn.preprocessing import StandardScaler


Scaling is a special case of *normalizing* the data.
There are many other normalization methods.
We will see some of them later in the course.



Log-Transform to predict Count Data
-----------------------------------

Count data is often evaluted with the `Root Mean Squared Log Error (RMSLE) <https://www.kaggle.com/c/bike-sharing-demand/overview/evaluation>`_.

The purpose of this metric is to treat the error in relation to the absolute value.
If the predicted value is 100, an error of 10 does not matter that much,
but if the predicted value is only 1, the same error is huge. The logarithm fixes that.

To optimize your model against the RMSLE, you should take the logarithm of the target colum (`y`).
Because 0 is a valid target value, use the log of :math:`y+1` instead:

.. code:: python3

   ylog = np.log1p(y)

Then train your model on the transformed column ``ylog``. To bring back your `log` predictions
to the original scale you have to apply the inverse transformation on the predictions:

.. code:: python3

   ypred_log = m.predict(X)
   ypred = np.exp(ypred_log)-1

You can then calculate the RMSLE score using sklearn:

.. code:: python3

   from sklearn.metrics import mean_squared_log_error

   np.sqrt(mean_squared_log_error(y, ypred))

.. warning::

   The log transformation only makes sense if there is an absolute zero. 
   This is the case with countable quantities (products sold, money, stocks, movies, electrons).
   It does not work with uncountable ones (Celsius temperature, timestamps).


pandas functions for Feature Engineering
----------------------------------------

Many pandas functions are very useful for feature engineering as well.
They are a good starting point if you want to write your own ``FunctionTransformer``.

=================================== ================================
function                            description
=================================== ================================
:py:meth:`pandas.DataFrame.fillna`  imputation
:py:func:`pandas.get_dummies`       one-hot encoding
:py:func:`pandas.cut`               binning (bins of equal width)
:py:func:`pandas.qcut`              binning (quantile bins)
:py:meth:`pandas.Series.factorize`  convert a category to an integer
=================================== ================================


   Count data is often evaluted with the `Root Mean Squared Log Error (RMSLE) <https://www.kaggle.com/c/bike-sharing-demand/overview/evaluation>`_.

   The purpose of this metric is to treat the error in relation to the absolute value.
   If the predicted value is 100, an error of 10 does not matter that much,
   but if the predicted value is only 1, the same error is huge. The logarithm fixes that.

   To optimize your model against the RMSLE, you should take the logarithm of the target colum (`y`).
   Because 0 is a valid target value, use the log of :math:`y+1` instead:

   .. code:: python3

      ylog = np.log1p(y)

   Then train your model on the transformed column ``ylog``. To bring back your `log` predictions
   to the original scale you have to apply the inverse transformation on the predictions:

   .. code:: python3

      ypred = np.exp(ypredlog)-1

   You can then calculate the RMSLE score using sklearn:

   .. code:: python3

      from sklearn.metrics import mean_squared_log_error

      np.sqrt(mean_squared_log_error(y, ypred))

   .. warning::

      The log transformation only makes sense if there is an absolute zero. 
      This is the case with countable quantities (products sold, money, stocks, movies, electrons).
      It does not work with uncountable ones (Celsius temperature, timestamps).
