
# Lyrics Classification

1. load the JSON file with lyrics
2. inspect a few entries
3. build a list of artists y
4. build a list of song lyrics X
5. make sure X and y have the same length
6. use scikit to do a train-test split
7. create a sklearn.feature_extraction.CountVectorizer
8. transform X into word counts Xw
9. train a RandomForest on Xw and y
10. calculate a training and test accuracy
11. Predict for a sample sentence

Optional:
- check the shape of Xw
- convert all lyrics to lowercase
- try different options for tokenization () and stop words ("english")
- try the TFIDFVectorizer instead
- train a Dense neural network on Xw
