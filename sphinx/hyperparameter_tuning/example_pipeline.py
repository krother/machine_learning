
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model_pipe = make_pipeline(
        MinMaxScaler(),
        LogisticRegression()
      )

model_pipe.fit(X, y)
model_pipe.score(X, y)

scores = cross_val_score(model_pipe, X, y)

print(scores)
