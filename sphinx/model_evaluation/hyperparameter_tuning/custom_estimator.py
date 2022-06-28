
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
from sklearn.base import BaseEstimator, TransformerMixin


class FillMissingValues(BaseEstimator, TransformerMixin):

     def __init__(self, strategy='mean'):
         """Store the hyperparameters"""
         self.strategy = strategy

     def fit(self, X):
         self.mean_ = X.mean()
         return self

     def transform(self, X):
         return X.fillna(self.mean_)

     def get_params(self, deep=True):
         """Scikit requires us to return a dictionary here"""
         return {"strategy": self.strategy}

     def set_params(self, **parameters):
         """Scikit uses this to set parameters"""
         for parameter, value in parameters.items():
             setattr(self, parameter, value)
         return self


import pandas as pd
import numpy as np

X = pd.Series([1, 3, np.NaN, 4, 0])
m = FillMissingValues()
m.fit(X)
print(m.transform(X))

# use ClassifierMixin in you want to create your own model
#  (needs to have a predict() method)
