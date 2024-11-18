
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn import svm

model = Pipeline([
        ('scaler', MinMaxScaler()),
        ('svc', svm.SVC(kernel='linear', C=1.0)),
    ])

model.fit(X, y)

print(model.score(X, y))
