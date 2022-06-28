
Missing Values
--------------

Many feature columns contain empty values.
Removing the rows with missing values is often not an option,
e.g. if you anticipate that there could be missing data that you need to handle
in the test set, anyway.

**Imputation** is a generic term for methods that fill the gaps instead.

The example fills a single missing value in the **Embarked** column:

.. code:: python3

   from sklearn.impute import SimpleImputer

   imputer = SimpleImputer(strategy='most_frequent')
   imputer.fit(X[['Embarked']])        # learn the most frequent value
   imputer.transform(X[['Embarked']])  # transform the column

With numerical columns you can also use ``"mean"`` or ``"median"`` as strategies.


.. container:: banner reading

   Other imputation strategies

.. highlights::

   There is a multitude of other imputation strategies:

   -  insert the next or last known value (:py:meth:`pandas.DataFrame.fillna`)
   -  interpolate (:py:meth:`pandas.Series.interpolate`)
   -  insert the mean/median by a category (with ``df.groupby().transform()``)
   -  K-nearest neighbor (implemented in the `FancyImputer package <https://github.com/iskandr/fancyimpute>`__)
   -  also see `advanced strategies in scikit <https://scikit-learn.org/stable/modules/impute.html#impute>`__
