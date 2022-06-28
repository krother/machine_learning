
import numpy as np
from sklearn.decomposition import NMF
import pandas as pd

# movie, ratings by users
data = [
    [5, 4, 1, 1, 3],
    [3, 2, 1, 3, 1],
    [3, 3, 3, 3, 5],
    [1, 1, 5, 4, 4],
]
columns = ['Titanic', 'Tiffany', 'Terminator', 'Star Trek', 'Star Wars'] #movies
index = ['Ada', 'Bob', 'Steve', 'Margaret'] #users

#need a dataframe for this
R = pd.DataFrame(data, index=index, columns=columns).values

#create a model and set the hyperparameters
# model assumes R ~ PQ'
model = NMF(n_components=2, init='random', random_state=10)

model.fit(R)

Q = model.components_  # movie-genre matrix

P = model.transform(R)  # user-genre matrix

print(model.reconstruction_err_) #reconstruction error

nR = np.dot(P, Q)
print(nR) ## The reconstructed matrix!

# predict the hidden features for a new data point
query = [[1, 2, 5, 4, 5]]
#in this case, a new user providing ratings for the 5 movies.
print(model.transform(query))
