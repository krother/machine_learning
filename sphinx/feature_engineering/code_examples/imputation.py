"""

Imputation

https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html

fill in missing values

1. Execute the code 
   (in Jupyter, split it into multiple cells)

2. Understand what is happening
   QUESTION: What other imputation strategies exist (check out the "strategy" parameter in the documentation)?

3. Explain to the rest of the group what you did
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


df = pd.read_csv('all_penguins_clean.csv', na_values='.')


imputer = SimpleImputer(strategy='most_frequent')
cols = df[['Sex']]

# count the number of missing values
print(cols['Sex'].isna().sum())


imputer.fit(cols)            # learn the most frequent value
t = imputer.transform(cols)  # result is a numpy array
print(t.shape)
print()

# format output as a DataFame
cols_imputed = pd.DataFrame(t, columns=cols.columns)
print(cols_imputed.head())
print()
