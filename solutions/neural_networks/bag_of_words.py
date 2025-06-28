
import json
from pprint import pprint
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier

corpus = json.load(open(r"C:\Users\team-\Desktop\aiclass\lyrics.json"))
pprint(corpus[0])

y = [doc["artist"] for doc in corpus]
X = [doc["text"] for doc in corpus]

from collections import Counter
print(Counter(y))

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)

cv = CountVectorizer(
    token_pattern= r"\b[a-z]{4,8}\b",
    stop_words="english",
    lowercase=True,
    )
cv.fit(Xtrain)
Xw_train = cv.transform(Xtrain)
Xw_test = cv.transform(Xtest)
# print(cv.vocabulary_) # word list
print(Xw_train.shape)

from sklearn.linear_model import LogisticRegression
# lower C = more regularization
model = LogisticRegression(C=0.000000001, class_weight="balanced")
model.fit(Xw_train, ytrain)
print(model.score(Xw_train, ytrain))

print(cross_val_score(model, Xw_train, ytrain, cv=5).round(2))

Xpred = ["dont worry about a thing because every little thing gonna be alright"]
Xpred = cv.transform(Xpred)
print(model.predict(Xpred))
print(model.classes_)
print(model.predict_proba(Xpred).round(3))
