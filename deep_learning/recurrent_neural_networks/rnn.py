
import numpy as np
import matplotlib.pylab as plt
from keras.models import Sequential
from keras.layers import RNN, SimpleRNN, SimpleRNNCell, Activation, Dense, LSTM
from keras.callbacks import TensorBoard
from keras import backend as K
import keras


K.clear_session()

#
# create sine wave sniplets
#
N = 1000
SEQLEN = 20

x = np.linspace(1.0, 100.0, N)
ytrue = np.sin(x)
y = ytrue #+ (np.random.random(N) - 0.5) / 2.0

# create 120 random sequences of length 10
starts = np.random.randint(1, N - SEQLEN, 120)
ends = starts + SEQLEN

samples = []
for s, e in zip(starts, ends):
    samples.append(y[s:e])
samples = np.array(samples)
X = samples[:,:SEQLEN - 1].reshape(120, -1, 1)
y = samples[:,SEQLEN - 1]
print(X.shape, y.shape)

Xtrain, ytrain = X[:100], y[:100]
Xtest, ytest = X[100:], y[100:]

model = Sequential([
    LSTM(1, input_shape=(None, 1), return_sequences=True),
    LSTM(1, return_sequences=False),
    Dense(1),
    Activation("linear")
])

model.compile(optimizer='adam', loss='mse')
model.summary()

model.fit(Xtrain, ytrain, epochs=50, batch_size=20,
          validation_split=0.2)

score = model.evaluate(Xtest, ytest, batch_size=10)
print(score)


ypred = model.predict(Xtest)
x = Xtest.reshape(20, SEQLEN - 1)
z = np.hstack((x, ypred))
xx = list(range(SEQLEN))

for i in range(10):
    plt.plot(xx, z[i])

plt.show()
