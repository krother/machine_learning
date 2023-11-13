"""
Hierarchical Clustering
"""
from dataclasses import dataclass
from itertools import combinations

from graphviz import Digraph


languages = {
    "english": ["mother", "pizza", "orange"],
    "polish": ["matka", "pizza", "pomarancza"],
    "croatian": ["matko", "pizza", "pomaro"],
    "german": ["mutter", "pizza", "orange"],
    "finnish": ["äiti", "pizza", "oranssi"],
    "french": ["mere", "pizza", "orange"],
}


@dataclass
class LeafNode:

    name: str
    words: list[str]

    def draw(self, graph):
        graph.node(self.name, self.name)


@dataclass
class InternalNode:

    name: str
    left: LeafNode
    right: LeafNode

    def draw(self, graph):
        self.left.draw(graph)
        self.right.draw(graph)
        graph.node(self.name, '', shape='point')
        graph.edge(self.name, self.left.name, dir='none')
        graph.edge(self.name, self.right.name, dir='none')



def get_similarity(node1, node2):
    # cluster linkage rule
    if isinstance(node1, InternalNode):
        return (
            get_similarity(node1.left, node2) +
            get_similarity(node1.right, node2)
        ) / 2
    elif isinstance(node2, InternalNode):
        return get_similarity(node2, node1)
    # actual language similarity
    word_sims = []
    for w1, w2 in zip(node1.words, node2.words):
        s1, s2 = set(w1), set(w2)
        sim = len(s1.intersection(w2)) / len(s1.union(s2))
        word_sims.append(sim)
    return sum(word_sims)


# 1. create a leaf node for every element of E.
nodes = [LeafNode(lang, words) for lang, words in languages.items()]

while len(nodes) > 1:
    # 2. find the pair of distinct elements (e1, e2) in E with the largest similarity
    best_sim = 0.0
    best_pair = None
    for e1, e2 in combinations(nodes, 2):
        sim = get_similarity(e1, e2)
        if sim > best_sim:
            best_sim = sim
            best_pair = e1, e2

    # 3. create a new internal node that contains e1 and e2
    e1, e2 = best_pair
    node = InternalNode(str(len(nodes)), e1, e2)
    print(f"new node {node.name} connecting {e1.name}, {e2.name}")
    nodes.append(node)
    nodes.remove(e1)
    nodes.remove(e2)

# draw the tree
tree = nodes[0]
graph = Digraph(
    edge_attr={'dir': 'back', 'color': 'black'},
    node_attr={'fontname': 'arial', 'color': 'lightblue', 'style': 'filled'}
)
tree.draw(graph)
graph.render('languages.gv', view=True)

