
Column Transformers and Pipelines
=================================

ColumnTransformers
------------------

The `ColumnTransformer` class is a central tool in `scikit-learn` to define 
which Feature Engineering method should be applied to which column.

To create a `ColumnTransformer`, you need to provide a list of transformers
with a ``(name, method, columns)`` tuple. The simplest transformer, ``passthrough`` 
does nothing to the specified columns. It is defined as follows:

.. code:: python3

   from sklearn.compose import ColumnTransformer

   trans = ColumnTransformer([      
       ('do_nothing', 'passthrough', ['col1', 'col2'])
   ])


Then you need to call ``fit()`` and ``transform()`` on your training data:

.. code:: python3

   trans.fit(Xtrain)                    # DataFrame with training data
   Xtrain_fe = trans.transform(Xtrain)  # use this to train your model


But **only** call ``transform()`` with data for testing or prediction, but not ``fit()``.
By the same logic you would not fit your model on test data either:

.. code:: python3

   Xtest_fe = trans.transform(Xtest)

The fit/transform logic applies to almost all preprocessing classes in scikit-learn.

.. code:: python3

   from sklearn.preprocessing import OneHotEncoder
   from sklearn.impute import SimpleImputer

   trans = ColumnTransformer([
       ('onehot', OneHotEncoder(sparse=False, handle_unknown='ignore'), ['col3']),
       ('missing', SimpleImputer(strategy='most_frequent'), ['col4']),
       ('do_nothing', 'passthrough', ['col1', 'col2']),
   ])



Custom Functions
----------------

Many Feature Engineering techniques do not have a scikit class ready.
Some of them highly depend on the dataset.

The ``FunctionTransformer`` allows you to wrap your own code in a function
and plug it into a ``ColumnTransformer``.
Your functions should accept a DataFrame as an argument and return a 2D array.

The following code calculates the length of a string as a feature:

.. code:: python3


   def name_length(df):
       length = df[df.columns[0]].str.len()
       return length.values.reshape(-1, 1)

To use the function without a `ColumnTransformer`, use:

.. code:: python3

   from sklearn.preprocessing import FunctionTransformer

   name_transformer = FunctionTransformer(name_length)
   name_transformer.fit(Xtrain[['name']])
   name_transformer.transform(Xtrain[['name']])

you can add the `FunctionTransformer` to your `ColumnTransformer`:

.. code:: python3

   ('name', FunctionTransformer(name_length), ['Name']),



Pipelines
---------

Sometimes, you need to apply two or more preprocessors at once. For example, you might
want to first impute missing values and then scale the column. 

A ``Pipeline`` allows you to run several preprocessors sequentially. You can combine
them as you like. 

.. code:: python3

   from sklearn.preprocessing import MinMaxScaler, SimpleImputer
   from sklearn.pipeline import make_pipeline

   impute_and_scale = make_pipeline(SimpleImputer(), MinMaxScaler())

   impute_and_scale.fit(X[['Age']])
   impute_and_scale.transform(X[['Age']])


Pipelines can also be included in a ``ColumnTransformer`` just like any other preprocessors.
This applies imputing and scaling sequentially to both the ``Age`` and ``Fare`` column.

.. code:: python3

   from sklearn.preprocessing import MinMaxScaler, SimpleImputer
   from sklearn.pipeline import make_pipeline

   impute_and_scale = make_pipeline(SimpleImputer(), MinMaxScaler())

   ...
   ('impute and scale', impute_and_scale, ['Age', 'Fare']),
   ...



.. hint::

   Things to check if your code does not work:

   -  print the shape of the transformed data after each step
   -  transform individul columns and inspect the result
   -  print the data after each step. Does it look as expected?
   -  check whether you call ``fit()`` and ``transform()`` with the right data.


.. seealso::

   This `lecture video by Andreas Müller <https://www.youtube.com/watch?v=XpOBSaktb6s>`__ covers a detailed explanation of pipelines and `ColumnTransformers`.

