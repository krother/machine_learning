.. _imbalance:


Class Imbalance
===============

.. figure:: scales.jpg

   *Photo by Elena Mozhvilo on Unsplash*

For a supervised classification problem, **class imbalance** means that the
number of samples/ observations from each class is not balanced. Often, we are
faced with one class that only has very few samples. This will negatively affect
the training phase of many machine learning algorithms. In the end,
classifiers will be biased towards the majority class: They favor the class
with more samples during prediction.

Note, that for many real-world problems, the issue is not the class imbalance itself.
It's the fact that we often only have very few samples in the **minority class**.
This makes it very difficult for any ML algorithm to properly distinguish between
the classes. The **decision boundaries** that are estimated by a
classifier become biased and do not properly separate the classes from each other.

In practice we have several options at hand to tackle the imbalance problem. They
can be categorized into methods that are applied **before**, **in between** or **after**
the training phase.


Strategies to deal with imbalanced classes
------------------------------------------

================================ ==========================================================================================
concept                          description
================================ ==========================================================================================
Class weights                    Assign higher weights to observation from the minority class during training
Oversampling                     Balance the *training* set by increasing the number of observations in the minority class
Undersampling                    Balance the *training* set by reducing the number of observations in the majority class
SMOTE                            A popular technique for over-sampling that generates new samples by interpolation
Precision-recall-curve           Calculates and plots the precision and recall scores for a range of threshold values
Threshold value                  Assign an observation to class ``1`` if the predicted score is larger the threshold
================================ ==========================================================================================


Class Weights
-------------

During training, each observation is multiplied by a weight that is inversely
proportional to the overall class frequency. This increases or decreases the
cost of miss-classification during training. Making a false guess for an observation
from the minority class becomes fare more costly! This procedure is also called
**cost sensitive learning**.

In scikit-learn we can apply weighting by setting the ``class_weights`` argument to ``'balanced'``:

.. code:: python3

      from sklearn.linear_model import RandomForestClassifier

      m = RandomForestClassifier(class_weight='balanced')
      m.fit(X, y)

The same is also possible for LogisticRegression and SVM classifiers.

In Logistic Regression the weight is applied by rescaling the `C`
hyperparameter in the loss function. The C parameter determines the strength of
regularization and the penalty that is given to false classifications
(figure taken from `here <https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html>`__):

.. figure:: https://scikit-learn.org/stable/_images/sphx_glr_plot_weighted_samples_001.png


Oversampling
------------

The goal of sampling is to draw a balanced sample of the **training** dataset for which each class
has roughly the same number of observation. We only apply sampling to
the training data and **not** to the test data. Because in the end, we have to evaluate
our classifier using real world conditions.

.. container:: banner python

   imbalanced-learn

.. highlights::

   `imbalanced-learn <https://imbalanced-learn.readthedocs.io/en/stable/index.html>`__
   contains various advanced implementations for over- and undersampling. The package
   integrates nicely into the scikit-learn pipeline.


Random oversampling draws a random sample with replacement from the minority class
until the dataset becomes balanced. We can then fit a classifier on the resampled
data:

.. code:: python3

      from imblearn.over_sampling import RandomOverSampler

      ros = RandomOverSampler()
      X_resampled, y_resampled = ros.fit_resample(X, y)
      m.fit(X_resampled, y_resampled)


Try out other strategies such as the ``SMOTE`` or ``ADASYN`` sampler!

Undersampling
-------------

Undersampling removes some observations of the majority class until the dataset
becomes balanced. This strategy should only be applied in **data rich** situations:
Usually, you should never throw away data as it can always contain valuable information!

.. code:: python3

   from imblearn.under_sampling import RandomUnderSampler

   rus = RandomUnderSampler()
   X_resampled, y_resampled = rus.fit_resample(X, y)
   m.fit(X_resampled, y_resampled)

SMOTE
-----

Instead of simply including random points multiple times like in oversampling, SMOTE interpolates from existing points to generate new ones.
The result is that there are no duplicate points in the resulting training data.

.. code:: python3

   from imblearn.over_sampling import SMOTE
   sm = SMOTE()
   X_resampled, y_resampled = sm.fit_resample(X, y)
   m.fit(X_resampled, y_resampled)

SMOTE is regarded as a better alternative to oversampling by many data scientists, because it mitigates some of the sampling bias that may come with 



.. container:: banner debug

   Does Outlier Detection help?

.. highlights::

   If you are faced with severe class imbalance and very few samples of the
   minority class, ordinary supervised classification may not be the right
   choice for your imbalanced data problem. Instead, have a look at methods for
   `outlier or anomaly detection <https://scikit-learn.org/stable/modules/outlier_detection.html>`__.




.. container:: banner reading

   Further Reading

.. highlights::

   - `Natalie Hockham@PyData2015`: Machine learning with imbalanced data sets.
     Insights from real-world business problems:

   .. youtube:: X9MZtvvQDR4


.. container:: banner recap

   Recap Questions

.. highlights::

   - What happens if you train a model without fixing class imbalance?
   - Enumerate 3 approaches to fix class imbalance.
   - Why shouldn't you use classification accuracy when dealing with imbalanced data?
   - What is the disadvantage of undersampling?
   - Are there any advantages that might justify the use of undersampling in some cases?
