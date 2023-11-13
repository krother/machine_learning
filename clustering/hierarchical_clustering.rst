Hierarchical Clustering
=======================

In hierarchical (or agglomerative) clustering, all data points
start as their own cluster.
They are connected one by one into tree structures
until all data points belong to a single tree.

Pseudocode
----------

Here is a generic hierarchical clustering algorithm:

::

    1. create a list of leaf nodes E from all elements you want to cluster
    2. find the pair of most similar elements (e1, e2) in E
    3. create a new internal node that contains e1 and e2
    4. add the new node to E
    5. remove e1 and e2 from E
    6. repeat from step 2. until there is only one node in E

Exercise: Ancestral Tree of Languages
-------------------------------------

In this exercise, we will examine the ancestry of spoken languages.
We assume that all languages originate from one common ancestor in a tree-like manner
(i.e. there is no lateral transfer of words).

Step 1: Build a table with words
++++++++++++++++++++++++++++++++

Build a spreadsheet where you write the same words in as many languages as possible.
Use one column for each language.
The table should be complete.
There should be at least 25 words and 6+ different languages.

Load the table from a CSV file into Python using the `pandas` library:

.. code:: python3

   import pandas as pd

   df = pd.read_csv("myfile.csv")
   print(df)

Step 2: Similarity of words
+++++++++++++++++++++++++++

Implement a function that calculates the similarity of two words.
For a first implementation, we will match the occurence of characters,
ignoring their exact position:

.. math::

   sim = \frac{chars1 \cap chars2}{chars1 \cup chars2}

Complete the code using the terms: `float, set, return, union, word2`:

.. code:: python3

    def calc_word_similarity(word1: str, word2: str) -> ___:
        s1, s2 = ___(word1), set(___)
        ___ len(s1.intersection(w2)) / len(s1.___(s2))
    
Test the function with a few examples:

.. code:: python3

    assert calc_word_similarity("hello", "hello") == 1.0
    assert calc_word_similarity("home", "dome") == 0.8
    assert calc_word_similarity("spam", "eggs") == 0.0

Step 3: Similarity of languages
+++++++++++++++++++++++++++++++

To calculate the similarity of two languages, use the mean of all word similarities.
Sort the lines below and add the correct indentation:

.. code:: python3

    for w1, w2 in zip(words1, words2):
    from typing import Sequence
    sim = calc_word_similarity(w1, w2)
    def calc_language_similarity(words1: Sequence[str], words2: Sequence[str]) -> float
    from statistics import mean
    return mean(word_sims)
    word_sims = []
    word_sims.append(sim)
    
Test the function using the actual languages from the table:

.. code:: python3

   print(calc_language_similarity(df["English"], df["Polish"]))

Step 4: Distance matrix
+++++++++++++++++++++++

Calculate the similarity for all pairs of languages.
Put the results into a new table.
We will refer to this table as a **distance matrix**.

Complete the following code:

.. code:: python3

    languages = df.columns
    sims = []
    for lang1 in languages:
        row = []
        ...

    dist_matrix = pd.DataFrame(sims, index=languages, columns=languages)


Use the seaborn library to plot the distance matrix:

.. code:: python3

   import seaborn as sns

   sns.heatmap(dist_matrix)

Step 5: Tree data structure
+++++++++++++++++++++++++++

For the implementation of the hierarchical clustering, we define data types for the tree nodes.
It would be possible to implement everything with Python lists and dictionaries, but the code is likely to become a mess.

.. code:: python3

    from dataclasses import dataclass

    @dataclass
    class LeafNode:

        name: str
        words: list[str]


    @dataclass
    class InternalNode:

        name: str
        left: LeafNode
        right: LeafNode

Step 6: Hierarchical clustering
+++++++++++++++++++++++++++++++

Now we can implement the algorithm from the generic pseudocode:

.. code:: python3

    # 1. create a leaf node for every element of E.
    nodes = [LeafNode(lang, df[lang]) for lang in df.columns]

    # 2. find the pair of most similar elements (e1, e2) in E

    # 3. create a new internal node that contains e1 and e2
    
    # 4. add the new node to E
    
    # 5. remove e1 and e2 from E
    
    # 6. repeat from step 2. until there is only one node in E

.. warning::

   You will notice that the code will not run yet.
   Why do you think that is?

Step 7: Linkage rule
++++++++++++++++++++

To handle the joined nodes, we will need a helper function that defines how internal nodes are joined.
This is called a **linkage rule**, an important hyperparameter in hierarchical clustering.

Try the following code:

.. code:: python3

    def get_similarity(node1: Union[InternalNode, LeafNode],
                       node2: Union[InternalNode, LeafNode]) -> float:
        if isinstance(node1, InternalNode):
            return (
                get_similarity(node1.left, node2) +
                get_similarity(node1.right, node2)
            ) / 2
        elif isinstance(node2, InternalNode):
            return get_similarity(node2, node1)
        else:
            return calc_language_similarity(...)

Now the algorithm should run.

Try to pretty-print the last remaining node.
You should see something that looks remotely similar to a tree:

.. code:: python3

    from pprint import pprint

    pprint(nodes)


Step 8: Draw the tree
+++++++++++++++++++++

To draw the tree, we will use the **pygraphviz** library.
Install it with:

::
    
    pip install pygraphviz

To make the drawing easier to implement, we tell the leaves and nodes to draw themselves.
Add a `draw()` method to the `LeafNode` class:

.. code:: python3

    def draw(self, graph):
        graph.node(self.name, self.name)

We do the same for `InternalNode`:

.. code:: python3

    def draw(self, graph):
        self.left.draw(graph)
        self.right.draw(graph)
        graph.node(self.name, '', shape='point')
        graph.edge(self.name, self.left.name, dir='none')
        graph.edge(self.name, self.right.name, dir='none')

If everything goes well, we can have a main drawing function take care of the styling:

.. code:: python3

    from graphviz import Digraph

    def draw_tree(nodes):
        """uses Graphviz to draw a tree on screen"""
        tree = nodes[0]
        graph = Digraph(
            edge_attr={'dir': 'back', 'color': 'black'},
            node_attr={'fontname': 'arial', 'color': 'lightblue', 'style': 'filled'}
        )
        tree.draw(graph)
        graph.render('languages.gv', view=True)



Caveats
-------

There exist many variations of the hierarchical clustering idea.
You can see the **distance metric** and **linkage rule** as hyperparameters.

In hieararchical clustering, you can decide *after* the clustering,
how many clusters you want to have.
To get **k** clusters, you would remove the **k** connections 
that were added last.
