
import numpy as np
import matplotlib.pylab as plt

N = 100

x = np.linspace(0.0, 50.0, N)
y = np.sin(x)

high = y > 0.5
low = y < -0.5
med = ~(high | low)

x1 = y.copy()
x2 = y.copy()
x3 = y.copy()

x1[low|med] = 0.0
x2[med|high] = 0.0
x3[low|high] = 0.0

X = np.array(list(zip(x1, x2, x3)))[:-1]
y = y[1:]

x = x[:-1]
plt.plot(x, X[:,0], 'r-')
plt.plot(x, X[:,1], 'b-')
plt.plot(x, X[:,2], 'g-')
plt.plot(x, y, 'k--')
plt.show()

# create random sequences
NUM_SEQS = 60
SEQLEN = 5

starts = np.random.randint(1, N - SEQLEN, NUM_SEQS)
ends = starts + SEQLEN

seqs = []
targets = []

for s, e in zip(starts, ends):
    seqs.append(X[s:e])
    targets.append(y[s:e])

X = np.array(seqs)
y = np.array(targets)

Xtrain, ytrain = X[:50], y[:50]
Xtest, ytest = X[50:], y[50:]

from keras.models import Sequential
from keras.layers import RNN, SimpleRNN, SimpleRNNCell
from keras.layers import Activation, Dense, Flatten, Input
from keras.layers import TimeDistributed, Reshape
from keras.callbacks import TensorBoard
import keras
import keras.backend as K

K.clear_session()

rc = SimpleRNNCell(1, activation="tanh")

# seq2seq implementation
model = Sequential([
    RNN(rc, return_sequences=True, input_shape=(SEQLEN, 3)),
    TimeDistributed(Dense(1, activation="linear")),
])

# seq2vec variant
model = Sequential([
    RNN(rc, return_sequences=True, input_shape=(SEQLEN, 3)),
    Flatten(),
    Dense(1, activation="linear")
])

# seq2seq encoder-decoder variant
"""
model = Sequential([
    RNN(rc, return_sequences=True, input_shape=(SEQLEN, 3)),
    Flatten(),
    Dense(SEQLEN, activation="tanh"),
    Reshape((SEQLEN, 1)),
    TimeDistributed(Dense(1, activation="linear")),
])
"""

model.compile(optimizer='adam', loss='mse')
model.summary()

model.fit(Xtrain, ytrain.reshape(50, SEQLEN, 1), epochs=200, batch_size=10)
#model.fit(Xtrain, ytrain[:,4], epochs=200, batch_size=10)

score = model.evaluate(Xtest, ytest.reshape(10, SEQLEN, 1), batch_size=10)
#score = model.evaluate(Xtest, ytest[:,4], batch_size=10)
print(score)

X = np.array(list(zip(x1, x2, x3)))[:-1]
y = []

for i in range(60):
    indata = X[i:i+SEQLEN].reshape(1, SEQLEN, 3)
    ypred = model.predict(indata, batch_size=1)
    y.append(ypred[0, SEQLEN-1, 0])
plt.figure()
plt.plot(range(60), y)
plt.show()
