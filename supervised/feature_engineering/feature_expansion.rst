Feature Expansion
-----------------

Polynomial terms
++++++++++++++++

Polynomial terms ar extra features that are the square or higher powers of an existing feature.

.. code:: python3

   from sklearn.preprocessing import PolynomialFeatures

   X = pd.DataFrame({'a': [1.0, 2.0, 3.0, 4.0]})
   m = PolynomialFeatures(degree=3)
   m.fit_transform(X)

Adding more features this way may increase the accuracy of your model. It also increases the risk of overfitting.

Interaction terms
+++++++++++++++++

**Interaction terms** are extra features that result from the product of two existing features.

.. code:: python3

   X = pd.DataFrame({
         'a':[1.0, 2.0, 3.0],
         'b':[1.0, 2.0, 0.0]})
   m = PolynomialFeatures(interaction_only=True)
   m.fit_transform(X)


.. hint::

   To combine polynomial features and interaction terms, leave away the `interaction_only` option.

