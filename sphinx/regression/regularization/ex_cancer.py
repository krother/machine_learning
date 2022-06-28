from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression

X, y = load_breast_cancer(True)

m = LogisticRegression()
m.fit(X, y)
print(score(X, y))

print(m.coef_[0])
