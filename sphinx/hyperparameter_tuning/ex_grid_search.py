from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
import pandas as pd

bca = datasets.load_breast_cancer()

X = bca.data[:,:2]  # only two features
y = bca.target

svc = svm.SVC()

grid = GridSearchCV(svc,
        param_grid={'C': [1.0, 0.1, 0.01, 0.001], 'kernel':['linear', 'rbf']},
        scoring='accuracy',
        n_jobs=1,
        cv=5,
        return_train_score=True
        )

grid.fit(X, y)
print("all scores      :")
print(pd.DataFrame(grid.cv_results_))

print("\nbest score      :", grid.best_score_)
