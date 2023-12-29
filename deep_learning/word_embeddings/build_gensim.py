
from gensim.models import word2vec

corpus = [
   "She loves you yeah yeah yeah",
   "see you later alligator",
   "see you later crocodile",
   "i just call to say i love you",
   "and it seems to me you lived your life like a candle in the wind",
   "baby you can drive my car",
   "we all live in the yellow submarine"
]

tokenized = [s.lower().split() for s in corpus]

wv = word2vec.Word2Vec(tokenized, size=7, window=5, min_count=1)
words = list(wv.wv.vocab)
len(words)

print(wv['crocodile'])

wv.wv.most_similar('crocodile')
