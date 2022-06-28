
.. _bow:

Bag of Words
============

.. image:: bag_of_words.jpg
    :width: 502px
    :height: 516px

*Photo by Alona Po on Unsplash*

**Bag of Words** is a method that converts a text corpus into a numerical matrix,
so that Machine Learning metods can use it as training data.


============= ============================================
concept       description
============= ============================================
Corpus        a list of strings (text documents)
Tokenization  dividing a text into words (or other units)
Vectorization converting text into numbers
Stop words    frequent words that carry little meaning
Stemming      cutting off word endings
n-grams       tokenizing into strings with n words
TF-IDF        method for normalizing counts
============= ============================================

.. container:: banner warmup

   Bag of Words from Scratch

.. highlights::

    **Step 1**:

    Build a simple text corpus with 5-10 sentences as a list of strings.

    .. hint::

       *"Text corpus"* is a term used by NLP practitioners. Most of the time it means *"a list of strings"*, where each string is called a *"document"*.

    **Step 2**:

    -  convert each string to lower case
    -  tokenize each string into a list of words (use the ``.split()`` method of strings).

    **Step 3**:

    Filter the words:

    -  remove short words
    -  remove numbers
    -  remove special characters

    **Step 4**:

    Count the occurrence of each word in each document.
    Use the ``collections.Counter`` dictionary:

    .. code:: python3

       from collections import Counter

       c = Counter(["apple", "apple", "pear"])

    **Step 5**:

    Build a DataFrame where each word is a column and each row is a document.
    The values should be the counts of a given word.

----

.. _bow_lyrics:

.. container:: banner milestone

   BoW in Scikit-Learn

.. highlights::


    **Step 1**:

    Use the ``CountVectorizer`` from Scikit to transform your corpus into a matrix.

    **Step 2**:

    Normalize the counts using the ``TfidfTransformer``.

    The TF-IDF uses the **Term Frequency (TF)** and the **Inverse Document Frequency (IDF)**
    of a word to adjust for words that are generally more frequent.

    .. math::

       TFIDF = TF(t, d) * (log \frac{1 + n}{1 + df(d, t)} + 1)

    * *TF(t, d)* is the number of times term t occurs in document d
    * *df(d, t)* is the number of documents containing term t
    * *n* is the number of documents

    **Step 3**:

    Print the total vocabulary size (an attribute of the vectorizer).

    **Step 4**:

    Try different values for the
    ``CountVectorizer`` (e.g. ``stop_words``, ``min_df``, ``ngram_range``).

    **Step 5**:

    Build a scikit-learn pipeline of the two transformers.


.. container:: banner challenge2

   TF-IDF from Scratch

.. highlights::

   Write your own TF-IDF algorithm.


.. container:: banner challenge3

   Topic Modeling

.. highlights::

   Apply **Latent Dirichlet Allocation** to identify 10 common ‘topics’ for one artist.

   Follow the `LDA Example on sklearn <https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html#sphx-glr-auto-examples-applications-plot-topics-extraction-with-nmf-lda-py>`__

----

.. container:: banner reading

   Links

.. highlights::

   -  `Lecture on Tf-Idf <http://www.cs.pomona.edu/~dkauchak/classes/f09/cs160-f09/lectures/lecture5-tfidf.pdf>`__
   -  The `Apache SpamAssassin datasets <https://spamassassin.apache.org/publiccorpus/>`__.

.. container:: banner recap

   Recap Questions

.. highlights::

   -  What are the strengths and weaknesses of the Bag of Words approach?
   -  What is tokenization?
   -  What are n-grams?
   -  Why are stop words often removed?
   -  What is the difference between stemming and lemmatization?
   -  Why is TF-IDF useful?
   -  Can you use a Bag of Words with other methods than NaiveBayes?
   -  what is a sparse matrix?
