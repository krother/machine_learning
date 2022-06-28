"""
Example:

running a Cross-Validation with Scikit-learn.
"""

from sklearn import svm, datasets
from sklearn.model_selection import cross_val_score


bca = datasets.load_breast_cancer()

X = bca.data[:,:2]  # only two features
y = bca.target

svc = svm.SVC(kernel='linear', C=1.0, probability=True)

# do a five-fold cross-validation
acc = cross_val_score(svc, X, y, cv=5, scoring='accuracy')

print("\naccuracy :", acc)
