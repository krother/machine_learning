"""
Hierarchical Clustering
"""
from dataclasses import dataclass
from itertools import combinations

from graphviz import Digraph


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
    ...



# draw the tree
tree = nodes[0]
graph = Digraph(
    edge_attr={'dir': 'back', 'color': 'black'},
    node_attr={'fontname': 'arial', 'color': 'lightblue', 'style': 'filled'}
)
tree.draw(graph)
graph.render('languages.gv', view=True)

