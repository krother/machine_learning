"""

Pipeline

https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html

apply several preprocessors sequentially

1. Execute the code 
   (in Jupyter, split it into multiple cells)

2. Understand what is happening

3. Explain to the rest of the group what you did
"""

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.pipeline import make_pipeline

df = pd.read_csv('all_penguins_clean.csv', na_values=".")


# define a pipeline
impute_and_encode = make_pipeline(
    SimpleImputer(strategy='most_frequent'), 
    OneHotEncoder(sparse=False)
)

cols = df[['Sex']]


impute_and_encode.fit(cols)             # apply .fit() of each preprocessor sequentially
t = impute_and_encode.transform(cols)   # apply . transform() sequentially
print(t.shape)
print()

# create a DataFrame
cols_transformed = pd.DataFrame(t, columns = impute_and_encode[1].get_feature_names())
print(cols_transformed.head())
