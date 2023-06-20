
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data[:,:2]
y = iris.target