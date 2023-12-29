Gradient Boosting
=================

.. image:: grad_boost_cover_photo.jpg
    :width: 545px
    :height: 580px

*Photo by Bill Jelen on Unsplash*

Gradient Boosting is an ensemble learning strategy that trains many weak models. 
Each model attempts to correctly predict the data points that previous models got
wrong.

Gradient Boosting has been used for models with extraordinary accuracy. 

The Boosting Algorithm
----------------------

Here is a simplified version of the Gradient Boosting Algorithm:

1. Get the data 
2. Start with an initial prediction
3. Calculate the loss (e.g. GINI or MSE)
4. Calculate the pseudo-residuals for each data point
5. Train a new shallow decision tree (weak learner) to predict the pseudo-residuals
6. Make new predictions by summing up the predictions of all trees trained so far
7. Repeat steps 3-6

**"Zooming In":** How to "boost" the predictive power of an ensemble of
many weak learners in series.

.. highlights::

    .. image:: gradient_boosting_whiteboard2.png




Key Concepts
------------

============================= ===========================================================================================
concept                       description
============================= ===========================================================================================
Loss (or Cost/Error) Function Function / metric to quantify how close the prediction is to the target.
Gradient                      First-order derivative a the loss function.
Pseudo-Residuals              Gradient of the loss function with respect to the predictions.
Boosting                      Ensemble technique to stack weak learners (i.e. models) in series (e.g. Gradient Boosting).
Bagging                       Ensemble technique where models train in parallel (e.g. Random Forest).
============================= ===========================================================================================


Catboost
--------

Catboost, developed by Yandex in 2017 is one of the most advanced implementations of Gradient Boosting.
The library features:

- symmetric, shallow trees
- efficient use of GPUs
- compatible to scikit-learn
- built-in tools: early stopping ("Overfitting Detector"), Shapley values, handling of missing values

The main strength is to deal with categorical features efficiently. 
The main problem with categories is that they need to be one-hot encoded first in other tree models.
One-hot encoding can lead to an explosion of the feature number, slowing down training and is prone to overfitting.

Catboost approaches this problem by calculating a single feature for each category (as one of the main strategies).
The dataset is permuted randomly several times, and a progressive label-based statistic is calculated for each permutation.

.. seealso::

   `Catboost notebook <code: https://github.com/catboost/tutorials/blob/master/events/2019_pydata_london/pydata_london_2019.ipynb>`__

.. container:: banner reading

   Links

.. highlights::

   -  `Catboost Documentation <https://catboost.ai/en/docs/concepts/algorithm-main-stages_cat-to-numberic>`__   
   -  `Bagging and Boosting <https://quantdare.com/what-is-the-difference-between-bagging-and-boosting/>`__
   -  `Gradient Boosting explained <https://explained.ai/gradient-boosting/index.html>`__
   -  `The New Generation of Gradient Boosting <https://towardsdatascience.com/https-medium-com-talperetz24-mastering-the-new-generation-of-gradient-boosting-db04062a7ea2>`__


.. container:: banner recap

   Recap Questions

.. highlights::

   - How exactly do models build on top of each other in Gradient Boosting?
   - What problems may occur when there are very many features?
   - Can you speed up training of Gradient Boosting by training each tree on multiple processors or machines?
   - What is the difference between bagging and boosting?
