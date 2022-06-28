
.. _ts_evaluation:

Evaluating Forecasts
====================

.. container:: banner warmup

   Evaluation Metrics

.. highlights::

  Enumerate evaluation metrics for regression problems that you know.


Goal of Evaluation
------------------

Evaluation gives us an estimate of how well the model will perform on data it has not been trained on (unseen data).


Methods of Evaluation
---------------------

#. Choose an evaluation metric
#. Apply cross-validation on the training data using the chosen metric
#. Calculate the metric for the test dataset (only once!)

Cross-Validation for Forecasting
--------------------------------

Do you remember how cross-validation for cross-sectional data worked?

.. figure:: crossval.png

Does it work the same way for time series data?

If there is time dependence in the data and we model it, this will not work. In this case, we should do the following:

.. figure:: tssplit.png

Alternative Evaluation Metrics - Information Criteria
-----------------------------------------------------

Akaike Information Criterion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   AIC = 2*k - 2*ln(\hat{L})

where *k* is the number of estimated parameters in the model and :math:`\hat{L}` is the maximum value of the likelihood function for the model.

- A lower AIC is better
- **k** penalizes overfitting
- The value of the likelihood function penalizes underfitting


.. container:: banner reading

   Further Reading

.. highlights::

   `Evaluating Model Fit <https://www.youtube.com/watch?v=xS4jDHQfP2o&t=85s>`__
