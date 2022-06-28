"""

One-Hot Encoding

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html

converts a categorical (nomial/ordinal) column to a matrix of binary variables

1. Execute the code 
   (in Jupyter, split it into multiple cells)

2. Understand what is happening

   QUESTION: Why do we convert to multiple columns?

3. Explain to the rest of the group what you did

"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('all_penguins_clean.csv')


# transform a categorical column
ohc = OneHotEncoder(sparse=False, handle_unknown='ignore')
cols = df[['Species']]
ohc.fit(cols)            # learn the classes
t = ohc.transform(cols)  # result is a numpy array
print(t.shape)
print()

# format output as a DataFame
species = pd.DataFrame(t, columns=ohc.get_feature_names())
print(species.head())
print()


# BONUS: include a second column

