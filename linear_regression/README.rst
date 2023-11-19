.. _linreg:

Linear Regression
=================

.. figure:: linear.png

Exercise: Linear Regression from Scratch
----------------------------------------

Below you find seven CSV files.
They contain artificial x and y data
(and a few common traps).

Download the **first data file** :download:`part1/linear01.csv` .
Inspect the data using the follwing code:

.. code:: python3

   import pandas as pd

   df = pd.read_csv("linear01.csv")
   print(df.columns)
   print(df.shape)

   df.plot.scatter(x="x1", y="y")

Then, write code that finds the optimal parameters of a line fitting the data.

Continue with the other six files:

* :download:`part1/linear02.csv`
* :download:`part1/linear03.csv`
* :download:`part1/linear04.csv`
* :download:`part1/linear05.csv`
* :download:`part1/linear06.csv`
* :download:`part1/linear07.csv`


Linear Regression models
------------------------

Linear Regression is a straightforward model predicting a **scalar value** from one or more features.
The basic idea is to fit a straight line to the data points.

.. math::

    \hat{y} = w_0 + w_1 x

- :math:`w_0` is called the **intercept** (or **bias**)
- :math:`w_1` is called the **slope** (**weight** or **coefficient**)

However, if you have multiple features, you would fit a plane or hyperplane instead.
With ``p`` features :math:`x_1, x_2 .. x_p`, each of them has one
**coefficient** :math:`w_1, w_2, ..., w_p` associated with it.
The model then becomes a weighted sum with a **parameter vector** :math:`w`:

.. math::

    \hat{y} = w_0 + w_1 x_1 + w_2 x_2 + \dots + w_p x_p


This equation can be written in a *vectorized* form, reducing the equation to a **dot product**:

.. math::

   \hat{y} =  \boldsymbol{X} \cdot \boldsymbol{w^T}


The Normal Equation
-------------------

There is an analytical solution that finds the parameters of a linear model
called the **Normal Equation** (or *closed form solution*).

.. math::

   \hat{w} = \frac{X^Ty}{X^TX}

However, the time to compute the Normal Equation grows to the power of 3 with the number of data points.
For many data points and/or features, the Normal Equation becomes very slow.
Also, it runs into a math dilemma (a non-invertible matrix) if the features are redundant
or linearly dependent.

In practice, you rarely find the Normal Equation, and the alternative **Gradient Descent** is used instead.


Evaluation Metrics
------------------

For calculation, the **Mean Squared Error (MSE)** is most commonly used.
The MSE is deeply rooted in the probability theory of linear models:

.. math::

   MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2

The MSE is deeply rooted in probability theory and helps to find the *most likely* model.
However, the **Mean Absolute Error (MAE)** is easier to interpret.
The MAE has the same unit as the target variable:

.. math::

   MAE = \frac{1}{n}\sum_{i=1}^{n}abs(y_i-\hat{y}_i)


The **coefficient of determination** :math:`R^2` tells you how much of the variance in your response can be explained by your features. 
So, a :math:`R^2` of 1.0 means your model has a perfect fit – no errors in your predictions!
On the other hand, a :math:`R^2` of 0.0 means your model is no better than a **simple average** over all points.
You can also think of this as comparing your predictions to the **simplest possible prediction: the average**.

.. math::

   R^2 = 1 - \frac{SSE}{SS_{total}} = 1 - \frac{\sum_{i=1}^n(y_i-\hat{y_i})^2}{\sum_{i=1}^n(y_i-\overline{y})^2}


Terminology
-----------

======================== ==================================================
concept                  description
======================== ==================================================
OLS                      Ordinary Least Squares, another name for Linear Regression
Normal Equation          analytical solution for Linear Regression (slow)
Gradient Descent         algorithm that finds a solution iteratively
MSE                      Mean Square Error
MAE                      Mean Absolute Error
GLM                      Generalized Linear Model, superfamily of OLS
Polynomial Regression    fitting polynomial features
======================== ==================================================


Example with Scikit
-------------------

.. literalinclude:: ex_linear_model.py

.. seealso::

   With good feature engineering, Linear Regression becomes a very strong technique for a variety
   of applications:

   `www.youtube.com/watch?v=68ABAU_V8qI <https://www.youtube.com/watch?v=68ABAU_V8qI>`__


Example with Statsmodels
------------------------

The ``statsmodels`` library gives you much more detailed output than scikit.

.. code:: python3

   X['intercept'] = 1

   m = OLS(endog=y, exog=X)
   r = m.fit()

   print(r.summary())
   ypred = r.predict(X)


Alternatively, you can specify an equation:

.. code:: python3

   m = OLS.from_formula('cnt ~ temp**2 + hum + windspeed', data=df)


Recap Questions
---------------

-  Can you use Linear Regression with millions of data points?
-  Can you use Linear Regression with millions of features?
-  Which training algorithms exist and what are their pros and cons?
-  Does it help to scale the date in Linear Regression?
-  How do Generalized Linear Models (GLMs) differ from linear regression?
