
from sklearn.datasets import make_moons
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz
import os

x, y = make_moons()

m = DecisionTreeClassifier(max_depth=3)
m.fit(x, y)


# create string in .dot format
tree = export_graphviz(m, out_file=None,
                class_names=["A", "B"],
                feature_names=['x1', 'x2'],
                impurity=False,
                filled=True)
open('moons.dot', 'w').write(tree)

graph = graphviz.Source(tree)
graph.render('moons')  # creates PDF
graph  # in Jupyter

# PNG conversion (tested on Ubuntu)
cmd = "dot -Tpng moons.dot -o tree_graphviz.png"
os.system(cmd)
