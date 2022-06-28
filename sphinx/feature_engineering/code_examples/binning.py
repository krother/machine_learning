"""

Binning

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html

converts a numerical column to a matrix of binary variables

1. Execute the code 
   (in Jupyter, split it into multiple cells)

2. Understand what is happening
   QUESTION: How does changing 'n_bins' affect the model?

3. Explain to the rest of the group what you did
"""

import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

df = pd.read_csv('all_penguins_clean.csv')
df = df.dropna() # drop all missing values


# transform a numerical column
kbins = KBinsDiscretizer(n_bins=5, encode='onehot-dense', strategy='quantile')

columns = df[['Culmen Length (mm)']]
kbins.fit(columns)
t = kbins.transform(columns)
print(t.shape)
print()



# BONUS: set the strategy parameter to 'uniform' and see how the edges change


# BONUS: create nice labels

edges = kbins.bin_edges_[0].round(1)
labels = []
for i in range(len(edges)-1):
    edge1 = edges[i]
    edge2 = edges[i+1]
    labels.append(f"{edge1}_to_{edge2}")

# create a DataFrame
df_bins = pd.DataFrame(t, columns=labels)
print(df_bins.head())

