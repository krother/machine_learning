"""

FunctionTransformer 

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html

applies a custom function to columns in your dataframe

1. Execute the code 
   (in Jupyter, split it into multiple cells)

2. Understand what is happening

3. Explain to the rest of the group what you did
"""

import pandas as pd
from sklearn.preprocessing import FunctionTransformer

df = pd.read_csv('all_penguins_clean.csv')

def custom_binner(x):
    bins = [-1, 10, 20, np.inf]
    labels = ['small', 'medium', 'large']
    x_binned = pd.cut(x, bins=bins, labels=labels, retbins=False)
    return pd.DataFrame({'x_binned':x_binned})  

# bin a numerical column
binner = FunctionTransformer(custom_binner)

cols = df[['Culmen Length (mm)']]

binner.fit(cols)               # learn the min and max of the data
t = binner.transform(cols)     # apply the transformation to the data
print(t.shape)
print()

# create a DataFrame
cols_scaled = pd.DataFrame(t, columns=cols.columns)
print(cols_scaled.head())
