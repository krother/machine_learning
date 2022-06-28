"""
From Joel Grus: Data Science from Scratch

https://github.com/joelgrus/data-science-from-scratch
"""
import math, random
from collections import defaultdict, Counter
from data import users_interests
from pprint import pprint


popular = Counter(interest for ui in users_interests
                           for interest in ui).most_common()

def most_popular_new_interests(user_interests, max_results=5):
    suggestions = [(interest, frequency)
                   for interest, frequency in popular
                   if interest not in user_interests]
    return suggestions[:max_results]


if __name__ == "__main__":

    print("Popular Interests")
    pprint(popular)
    print()

    print("Most Popular New Interests")
    print("already likes:", ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"])
    pprint(most_popular_new_interests(["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"]))
    print()
    print("already likes:", ["R", "Python", "statistics", "regression", "probability"])
    pprint(most_popular_new_interests(["R", "Python", "statistics", "regression", "probability"]))
    print()
