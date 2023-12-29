.. _naive_bayes:


Naive Bayes
===========

**Naive Bayes calculates a conditional probability based on observations.**


.. container:: banner warmup

   Priors and Posteriors

.. highlights::

   Assume there are 25 million programmers in the world.

   Estimate the probability that a random person is a programmer, if:

   *  you know nothing about them
   *  you know they are attending an university
   *  you know they are living in Romania


How The Baytles write songs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. highlights::

   .. figure:: baytles.png

A fictive band, *"The Baytles"*, write their songs like this:

-  they have a table with word probabilities
-  they generate words by rolling a dice
-  each word is independent of the previous words

The are the assumptions of a Naive Bayes model in a nutshell.

Pros and Cons of Naive Bayes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================ =============================================
Pros                             Cons
================================ =============================================
calculates probabilites          prior must be chosen
works even with small datasets   computationally intensive with large dataset
often very intuitive             tendency to overfit
================================ =============================================


The Bayes Theorem
~~~~~~~~~~~~~~~~~

Naive Bayes describes uses probabilities using the **Bayes Theorem**:

.. math::

   P(class|data) = \frac{P(data|class) * P(class)}{P(data)}

The Bayes Theorem is most useful if *P(data|class)* is easier to calculate than *P(class|data)*.

The probability, *P(class)* is called the **prior**. 
A prior is the assumed probability of an event before taking any data into account.
For instance, if we look at a set of songs, the probability that a song is by the Beatles depends on the distribution of artists in the dataset.

The **posterior probability** *P(class|data)* is the probability **after** looking at the data. It uses information from the data.
E.g., we would expect a higher posterior probility for a song being by the Beatles, if the word *yeah* occurs often.

.. math::

   P(class) = \frac{n_{class}}{n_{total}}


*P(data)* is called the *marginal probability*.
In a classifier, we can usually ignore the latter, because we only need to know the ratio between the classes.



How to calculate the conditional probability?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How can we calculate *P(data|class)*? You could calculate it from a table of counts.

But what if your data is a text document? What is the *probability of a document*?

One *naive* assumption is that the probability of the document is the combined probability
of all words that occur and that do not occur. We treat every word as an independent event.

In a way, we assume that the author of the document had a table with the probabilities of each word.
He then rolls dice many times to put together words at randon. A document has the following probability:

.. math::

   P(data) = P(word1) * P(word2) * P(word3) ... P(word n)

To calculate the probability of a particular document, we can calculate the probability
from the word counts (TF-IDF) in the training dataset for all words that occur in the document.

However, if a word does not occur in a document, you would use the inverse probability:

.. math::

   P(word) = 1 - word_frequency

With conditional probabilities it is the same.

.. warning::

   Of course, the words in most documents are **not** independent!
   This is why the method is called *naive*. It works quite well anyway.

What if one of the probabilities is zero?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
As soon as one probability is zero, the result will be zero as well.
This can be solved by adding a **smoothing term**.
Basically the smoothing term adds some number to every word count so that it never becomes zero.
This has a similar effect as a **regularization hyperparameter.**

In ``MultinomialNB``, use the hyperparameter ``C`` to control smoothing.

Isn't a product of many probabilities problematic?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you multiply many probabilities, the resulting number becomes **very** small.
This leads to issues with numerical precision when implementing it.

This can be solved painlessly by expressing the product as a **sum of log-probabilities**.
This works because:

.. math::

   log(p1 * p2 * p3 ..) = log(p1) + log(p2) + log(p3) ..


Naive Bayes in Scikit
~~~~~~~~~~~~~~~~~~~~~

For a classification with two or more classes you would want to use `MultinomialNB`:

.. code:: python3

   from sklearn.naive_bayes import MultinomialNB

   m = MultinomialNB(alpha=1.0)
   m.fit(...)

The `alpha` parameter is the regularization strength (it works in the same way as in Ridge/Lasso).


.. container:: banner reading

   Further Reading

.. highlights::

   **3blue1brown on Bayes Theorem**

   .. youtube:: HZGCoVF3YvM

   Also see `Chris Albons guide to implement Naive Bayes from
   scratch <https://chrisalbon.com/machine_learning/naive_bayes/naive_bayes_classifier_from_scratch/>`__



.. container:: banner recap

   Interview Questions

.. highlights::

   -  What is a prior?
   -  Explain the Bayes Theorem
   -  Explain the fundamentals of Naive Bayes? `[Answer] <https://www.analyticsvidhya.com/blog/2017/09/naive-bayes-explained/>`__
   -  When and why is Naive Bayes better than a Random Forest? `[Answer] <https://www.quora.com/When-and-why-is-a-naive-Bayes-classifier-a-better-worse-choice-than-a-random-forest-classifier>`__
