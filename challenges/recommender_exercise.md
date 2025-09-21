
# movie recommender from scratch

build a MR

### Movie Recommender 1: random

### Movie Recommender 2: find the best movies

find top 5 single ratings

sort by average rating

### Movie Recommender 3: also consider the number of votes


weigthed rating

WR = (v/(v+m))R+(m/(v+m))C

where:
R = average for the movie (mean) = (Rating)
v = number of votes for the movie = (votes)
m = minimum votes required to be listed in the Top 50 (currently 1000)
C = the mean vote across the whole report (currently 6.8) 

https://math.stackexchange.com/questions/169032/understanding-the-imdb-weighted-rating-function-for-usage-on-my-own-website

### Neighbourhood-based Search

k-NN

### search by similarity of users
to calculate the similarity of two users: try **cosine similarity**

u1 = "Hakan"
go through all users u2 (!= u1):
    calculate the similarity between u1 and u2 -> sim
    (0.0 dissimilar, 1.0 identical)
    find the user with the highest similarity -> u_best
   
sort the movies rated by u_best by rating
recommend a few of them