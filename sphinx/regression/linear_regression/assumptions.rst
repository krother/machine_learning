
.. _linreg_assumptions:

Evaluating Linear Regression Models
===================================

.. container:: banner warmup

   Anscombes Quartet

.. highlights::

   Explore an example dataset:

   .. code:: python3

      import seaborn as sns

      df = sns.load_dataset("anscombe")

   Calculate a few descriptive statistics:

   .. code:: python3

      df.groupby('dataset').describe()

   Also, plot the data:

   .. code:: python3

      df.groupby('dataset').plot.scatter('x', 'y')

   What do you notice?




Assumptions in Linear Regression
--------------------------------

There are eight assumptions in linear regression models that one might check:

=== ============================================================== =============================================================================================================== ================================================
Nr  Assumption                                                     Description                                                                                                     Importance
=== ============================================================== =============================================================================================================== ================================================
1)  Linear in parameters: :math:`Y = X \cdot w^T + \epsilon`         The true relationship between Y and X is linear in the parameters (+ some random error term :math:`\epsilon`) If violated, the model will be biased
2)  Random Sampling                                                The sample for the linear regression should be randomly chosen from the population                              If violated, the model will be biased
3)  Sample Variation in the Explanatory Variables X                The input variables X take on different values                                                                  If violated, there is no information to be gathered from the input X
4)  Zero Conditional Mean Assumption: E( :math:`\epsilon|X` ) = 0  The mean of the error term conditional on the input variables is zero                                           If violated, the model will be biased
5)  Homoscedasticity / Constant Variance                           The variance of the error term (Var(e)) is the same over all values of X                                        If violated, the model might not be efficient
6)  Normally distributed residuals                                 The distribution of the error term is (asymptotically) normal                                                   If violated, exact statistical statements about the coefficients are difficult
7)  No multicollinearity                                           The features of the model are not closely correlated with each other                                         If violated, p-values are useless
8)  No correlation between the error terms                         There is no autocorrelation between the error terms; mostly important for time series data                          If violated, exact statistical statements about the coefficients are difficult
=== ============================================================== =============================================================================================================== ================================================

The Gauss-Markov Theorem 
------------------------

The Gauss-Markov Theorem states that, if assumptions 1-5 hold, the linear regression model
derived by the OLS-Method is the **Best Linear Unbiased Estimator (BLUE)**. The
predicted values of Y will in expectation be equal to the true value of Y and
the estimator will have the lowest variance among all linear unbiased estimators.

If you are mainly interested in **predicting** values, checking assumptions 1-5 is sufficient.


Unbiasedness (Assumptions 1-4)
------------------------------

An estimate is said to be unbiased if, in expectation, it is equal to the true
value. For example:

:math:`E(\hat{w}|X) = w`

where :math:`\hat{w}` is the estimate of the coefficient w of the linear regression
and X are some input variables.

If assumptions 1-4 hold, linear regression will provide us with an
unbiased estimate of the coefficients :math:`\hat{w}` of the true coefficients w.
This in turn will also lead to an unbiased estimate of y.

:math:`E(\hat{y}|X)=X \dot  w^T=E(y|X)`

In words this means that, on average, the prediction :math:`\hat{y}` is
equal to the true value y.



Statistical Inference
---------------------

If assumptions 1-7 hold, a linear regression model can be used for **statistical inference**.

If, on top of predicting outcome values, we are interested in effect sizes (how much each feature contributes), assumptions 6) and 7) become important.
Especially assumption 6) makes statements about the distribution of the coefficient
estimates. According to assumption 6) they are normally distributed. This allows
us to construct confidence intervals and p-values.

The interpretability of confidence intervals and p-values can be influenced by
multicollinearity. If assumption 7) holds we don't have to worry about that.

How can we check whether the assumptions actually hold?


Checking Assumptions
--------------------

Check Assumption 1 - Linear relationship
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plot all the features against the target value Y:

.. code:: python3

   sns.pairplot(data)

Inspect the outcome visually. Ideally, you see more or less linear relationships
between the input features and Y. If not, then we can still linearize the
relationships. More on this in the next chapter `4.4 Feature Expansion and Reduction <http://krspiced.pythonanywhere.com/chapters/project_bicycles/feature_expansion_reduction.html>`__.


Check assumption 2 - Random Sampling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This assumption is hard to check. You need to have extensive knowledge about the
data collection process in order to answer the questions.


Check assumption 3 - Sample Variation in the input features X
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure that your input features X do not only have a single value.

.. code:: python3

  df[list_of_input_features].nunique()


Check assumption 4 - Zero Conditional Mean
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check that the mean error of your model is zero: :math:`E(\epsilon|X) = 0` .

If the residuals grow with any of your input variables, this assumption is violated.
Plotting the correlations with your residuals helps to find out:

.. code:: python3

   sns.residplot(X['temp'], y)

and

.. code:: python3

   sns.heatmap(X.corr(), annot=True)

The VIF (see below) also gives you an indication of this.


Check assumption 5 - Homoscedasticity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Homoscedasticity means that the residuals have the same variance for all values of X.
Lack of it (*heteroscedasticity*) means there may be patterns undescribed by your model.

You can check for homoscedasticity by plotting the residuals against X.
You should see random noise.

.. code:: python3

   plt.plot(X[:, 0], residuals)

There exist statistical tests for heteroscedasticity. Most notably we can use
the Breusch-Pagan test for heteroscedasticity. It is implemented in statsmodels.

.. code:: python3

  from statsmodels.stats.diagnostic import het_breuschpagan

A sufficiently small p-value implies that we can be quite sure to deal with
heteroskedasticity.


Check assumption 6 - Normally Distributed Residuals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The histogram of residuals gives you a good hint whether
the residuals are normally distributed or e.g. skewed.

.. code:: python3

   residuals.hist()

Another indication is the Q-Q-Plot.
It sorts the residuals and plots them against a normal distribution.
The residuals are ideally on a straight line:

.. code:: python3

   from scipy.stats import probplot
   import matplotlib.pyplot as plt

   probplot(residuals, plot=plt)


You can also run the Jarque-Bera test
(you can find it in the output of a `statsmodels` OLS model as well).

.. code:: python3

   from scipy.stats import jarque_bera

   jarque_bera(residuals)

It is good if the test statistic (first value) and the p-value (second value) are low.

Note that in large samples this assumption is not needed because we can use
the Central Limit Theorem (CLT) to establish asymptotic normality of the
errors.


Check assumption 7 - No Multicolinearity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If there is *multicolinearity* (you can express one feature by a combination of others)
the matrix *X* becomes non-invertible.

You can use the **Variance Inflation Factor (VIF)** to measure multicolinearity.
A VIF greater than 5 indicates high multicolinearity:

.. code:: python3

  from statsmodels.stats.outliers_influence import variance_inflation_factor
  from statsmodels.tools.tools import add_constant

  X = add_constant(X)
  pd.Series([variance_inflation_factor(X.values, i)
             for i in range(X.shape[1])],
            index=X.columns)

An easy solution for the problem of multicolinearity is to drop one of the
multicolinear features. This makes especially sense where we created the
multicolinearity ourselves by feature engineering (e.g. dummy variable trap).


Check assumption 8 - No autocorrelation of residuals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Autocorrelation means that the residuals do depend on each other systematically.
Typically you find autocorrelation when there is an inherent trend or
periodic pattern in the residuals.

Check this assumption with a Durbin Watson test or the ACF plot:

.. code:: python3

   from statsmodels.graphics.tsaplots import plot_acf

   plot_acf(residuals, lags=20)



.. container:: banner reading

   Further Reading

.. highlights::

   `OLS and the Gauss-Markov Theorem <https://www.statlect.com/fundamentals-of-statistics/Gauss-Markov-theorem>`__

.. container:: banner recap

   Recap Questions

.. highlights::

   -  Under what circumstances can you allow some assumptions to be violated?
   -  What do the numbers in the ``statsmodels`` output mean?

