"""
helper functions for the MovieLens dataset
"""
import os

import pandas as pd

from scipy.sparse import csr_matrix


BASE_PATH = os.path.split(__file__)[0] + '/../data/movielens_small/'



def preprocess_movies(min_ratings=20):
    """
    filter out movies rated by less or equal 'min_ratings' ... users
    and return a sparse user-item-matrix
    """
    ratings = pd.read_csv(BASE_PATH + 'ratings.csv')
    movies = pd.read_csv(BASE_PATH + 'movies.csv', index_col=0)

    ratings_per_movie = ratings.groupby('movieId')['userId'].count()

    # filter for movies with more than N ratings
    popular_movies = ratings_per_movie.loc[ratings_per_movie > min_ratings].index

    # only keep popular movies
    ratings = ratings.loc[ratings['movieId'].isin(popular_movies)]

    R = csr_matrix((ratings['rating'], (ratings['userId'], ratings['movieId'])))
    return ratings, movies, R


# sample query
DISNEY_MOVIE_IDS = [4470, 48, 594, 27619, 152081,595,616,1029]

# relevant hits for testing the recommender
DISNEY_RELEVANT_HITS = [
    596, 4016, 1033, 134853, 
    2018, 588, 364, 26999, 75395,2085, 
    1907, 2078, 1032, 177765   
]
