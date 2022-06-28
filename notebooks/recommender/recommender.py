
# Movie Recommender: sample solution

import pandas as pd
from sklearn.decomposition import NMF
import seaborn as sns
import numpy as np

df = pd.read_csv('ml-latest-small/ratings.csv')

del df['timestamp']

ratings = df.pivot('movieId', 'userId')
ratings.fillna(0.0, inplace=True)

m = NMF(n_components=20, init='nndsvd', random_state=42)
m.fit(ratings)

# Get movie titles
movies = pd.read_csv('ml-latest-small/movies.csv', index_col=0)
del movies['genres']


def get_id(s):
    result = movies[movies['title'].str.startswith(s)]
    print(result.values)
    return result.index[0]


def get_user_input(ratings):
    """user interface"""
    user = pd.Series(np.zeros(ratings.shape[0]), index=ratings.index)
    movie_name = ""
    while movie_name != 'x':
        movie_name = input('please enter a movie or x: ')
        if movie_name != 'x':
            user[get_id(movie_name)] = 5
    return user


def calculations(user):
    P = m.components_
    Q = m.transform(ratings)
    profile = np.dot(user, Q)
    ranking = np.dot(profile, Q.T)
    ranking = pd.Series(ranking, index=ratings.index)
    return ranking


def print_output(ranking):
    result = pd.DataFrame({'title': movies['title'], 'rank': ranking})
    result.sort_values('rank', ascending=False, inplace=True)
    print(result.head(20))


def main():
    query = get_user_input(ratings)
    result = calculations(query)
    print_output(result)


if __name__ == '__main__':
    main()  # not executed while importing
