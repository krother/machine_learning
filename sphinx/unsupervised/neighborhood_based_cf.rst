.. _neighborhood_based_cf:

Neighborhood-based Collaborative Filtering
==========================================

   `"Together we can be better, and together we'll better understand each other."`
   (`Kim Falk, 2019: Practical Recommender Systems <https://www.manning.com/books/practical-recommender-systems>`__)

We can broadly distinguish between **memory/neighborhood-based** and **model-based** methods:
The former use (pre-)calculated similarities between users and items to recommend new items to users. 
The latter use statistical models, such as `Non Negative Matrix Factorization (NMF) <model_based_cf.html>`_ to learn and predict ratings.

In a nutshell, for neighborhood-based CF, recommendations are derived by looking at the most similar entities:

.. figure:: collaborative_filtering.gif

Key Concepts
------------

================== ============================================================================
concept            description
================== ============================================================================
similarity score   a value that is higher if two users or items are more similar to each other
similarity matrix  a matrix that contains the pairwise similarity scores for each item or user
k-neighborhood     top k users or items that are most similar to a specific user or item
cold-start problem difficulty to recommend new items or to make recommendations to new users
active user        the current user that receives recommendations (e.g. a visitor of a website)
================== ============================================================================

.. container:: banner warmup

   Real-world Recommender Systems

.. highlights::

   Find real-world examples of personalized recommender systems with which you interact on a daily basis:

   - Which and how many items are recommended? Is there a ranking between the items?
   - How frequently do the recommondations change?
   - What could you possibly do, to change the items that are recommonded to you?
   - Are the recommondations based on explicit or implicit feedback? (Or something else?) 


Item-based and user-based filtering
-----------------------------------

With the user-item matrix at hand, we can generate recommendations for unseen items of the **active user** in two ways:

- We can select other *users* that showed similar activity and recommend the items that they have liked and that the active user hasn't seen yet.
- We can recommend unseen *items* that were rated similar to the items that the active user already liked.

For user-based filtering we calculate similarities between users. For item-based filtering we calculate similarities between items. 
In both cases we use the user-item rating matrix as the starting point.

Notation
~~~~~~~~

We write users with the subscripts `u` or `v` and movies/items with `i` or `j`.

========================= ====================================================================================
variable                  description
========================= ====================================================================================
:math:`r_{ui}`            rating of user u for movie i
:math:`\hat{r}_{ui}`      predicted rating of user u for movie i
:math:`sim(u,v)`          similarity between user u and user v
:math:`sim(i,j)`          similarity between movie i and movie j
:math:`N_i^k(u)`          k-neighborhood of *users* that are similar to user u and that rated movie i
:math:`N_u^k(i)`          k-neighborhood of *movies* that are similar to item i and that were rated by user u 
========================= ====================================================================================


Algorithm: user-based filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   *"Users who are similar to you also liked these movies"*


.. highlights::

   - Input: Active user *u*
   - Output: List of recommendations
   
   - **Offline**: Calculate pairwise similarities :math:`sim(u,v)` between all users
   - Optionally: Write the similarities to a db (as a long table with columns: `source`, `target`, `similarity`).

   1. Get a list of unrated items for the active user *u*
   2. For each unrated item *i*: 

      3. Select a k-neighborhood of users (e.g. top-20 users that are most similar to *u* and that have rated *i*).
      4. Calculate the predicted rating for the unseen item as the (weighted) average based on the neighborhood of users.

      .. math::

         \hat{r}_{ui} = \frac{\sum_{v \in N_i^k(u)} sim(u, v) r_{vi}}{\sum_{v \in N_i^k(u)} sim(u, v)}

   5. Sort the predicted ratings and return the top-N items as recommondations.


.. container:: banner math

   User-based collaborative filtering algorithm

.. highlights::

   - Calculate the user-user similarity matrix (see exercise above).
   - Pick an active user.
   - Find the top 10-20 most similar users to the active user.
   - With these subset of users, calculate the average rating.
   - Optionally: Use the distance to the active user as a weight when calculating the average. 
   - Recommend item that the similar users liked most and that the active user has not seen yet.


Algorithm: item-based filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   *"Based on your watched movies we can recommend these similar movies"*

.. highlights::

   - Input: Active user *u*
   - Output: List of recommendations

   - **Offline**: Calculate the pairwise similarities :math:`sim(i,j)`  between every item and all other items.
   - Optionally: Write the similarities to a db (as a long table with columns: `source`, `target`, `similarity`).

   1. Find a top-list of unrated *candiate items* that are similar to allready rated items
   2. For each item *i* in the candiate list:

      3. Select a neighborhood of items *rated by u* 
      4. Calculate the predicted rating for the unseen item *i* as the (weighted) average based on the neighborhood of items.

      .. math::

         \hat{r}_{ui} = \frac{\sum_{j \in N_u^k(i)} sim(i, j) r_{uj}}{\sum_{v \in N_u^k(i)} sim(i, j)}

   5. Sort the predicted ratings and return the top-N items as recommondations.


.. container:: banner math

   Item-based collaborative filtering algorithm

.. highlights::

   - Calculate pairwise similarities between all items.
   - Write the similarities to a db (as a long table with columns: `source`, `target`, `similarity`).
   - Present the users of your website similar items when they look up the details of an item.


.. container:: banner question

   How to deal with new users or items?

.. highlights::

   We shouldn't use CF for users that have only rated one or two items. 
   Similarly, we shouldn't calculate similarity scores for items that were only rated by a few users.
   This is the **cold-start problem**: There is no data to generate any recommendations and similarity scores will be unreliable.

   Here are some ideas to handle the cold start problem for either new users or new items:

   - show a global list of new or fresh items to the users
   - randomly place a few unknown items to the recommendations
   - ask users to rate a few items first before they can use the system
   - recommend the most popular items or suggest some random sampled items 
   - switch to `content based filtering <https://en.wikipedia.org/wiki/Recommender_system#Content-based_filtering>`__ or hybrid approaches




.. container:: banner question

   How to deal with missing values?

.. highlights::

   There is no preferred or right way of handling missing ratings in user or item based collaborative filtering.
   
   Here are some possible options:
   
   - Discard items/ users with missing values when calculating similarities between users/ items.
   - Fill all missing values with a default value (e.g. zero or the average rating).
   - Normalize the rating data by substracting each users' average rating from their rating vectors. Fill all missing values with zeros.
   - Try out different similarity metrics.


.. container:: banner debug

   Collaborative Filtering - Adjustments

.. highlights::

   Many factors such as the sparsity of the data, the scale of the ratings or the number of users and items can effect the 
   quality of recommondations. As we usually deal with user interactions in real-time, **performance** becomes as important as recommondation accuracy.
   
   Here are some questions to think about when designing a recommender system: 

   - Should you only consider positive or the most recent ratings?
   - Should you normalize the ratings (e.g. substract the users' average)? 
   - Which similarity measure should you use? How to store them efficiently for fast retrieval? 
   - How many users need to rate two movies such that their similarity score becomes reliable?
   - How many movies should two users have in common such that their similarity score becomes reliable?
   - How large should be k when computing the k-neighborhood?
   - Should you only return recommondations with above average predictions or all of them?



Examples
--------

-  Sample data :download:`data.py <data.py>`
-  Popularity-based filtering :download:`ex_popularity.py <ex_popularity.py>`
-  User-based filtering :download:`ex_user_based.py <ex_user_based.py>`
-  Item-based filtering :download:`ex_item_based.py <ex_item_based.py>`


.. include:: cosine_similarity.rst


  


.. container:: banner reading

   Links

.. highlights::

   -  `Implementations of Collaborative Filtering <https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0>`__
   -  `Challenges in recommenders <https://en.wikipedia.org/wiki/Collaborative_filtering#Challenges>`__
   -  `Crab <https://muricoca.github.io/crab/>`__
   -  `Netflix Prize <https://netflixprize.com/>`__
   -  `Deep Learning for Recommenders <https://arxiv.org/abs/1707.07435>`__
