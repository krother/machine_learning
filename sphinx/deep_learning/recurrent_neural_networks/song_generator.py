
from tensorflow.keras.callbacks import LambdaCallback
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.layers import LSTM
from tensorflow.keras.optimizers import RMSprop
import numpy as np
import random
import sys
import io


text = '''
What you want (oo)
Baby, I got (oo)
What you need (oo)
Do you know I got it? (oo)
All I'm askin' (oo)
Is for a little respect

when you come home (just a little bit)
Hey baby (just a little bit)
when you get home (just a little bit)
mister (just a little bit)

I ain't gonna do you wrong while you're gone
Ain't gonna do you wrong (oo)
'cause I don't wanna (oo)
All I'm askin' (oo)
Is for a little respect when you come home (just a little bit)
Baby (just a little bit)
when you get home (just a little bit)
Yeah (just a little bit)'''

# vary this to raise/lower randomness
DIVERSITY = 0.2

# create character lookup dictionary
chars = sorted(list(set(text)))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

# cut the text in semi-redundant sequences of maxlen characters
maxlen = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])

nseq = len(sentences)
nchars = len(chars)

print('number of sequences:', nseq)
print('corpus length:', len(text))
print('total chars:', nchars)

# vectorize sequences
x = np.zeros((nseq, maxlen, nchars), dtype=np.bool)
y = np.zeros((nseq, nchars), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1


# build the model: a single LSTM
print('Build model...')
model = Sequential()
model.add(LSTM(64, input_shape=(maxlen, nchars)))
model.add(Dense(nchars))
model.add(Activation('softmax'))

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)


def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def on_epoch_end(epoch, logs):
    # Function invoked at end of each epoch. Prints generated text.
    if epoch % 10 != 0:
        return
    # create a seed
    start_index = random.randint(0, len(text) - maxlen - 1)
    generated = ''
    sentence = text[start_index: start_index + maxlen]
    generated += sentence
    print(f'\nGenerating text after Epoch: {epoch} with seed: \n{sentence}\n')
    sys.stdout.write(generated)

    for i in range(300):
        x_pred = np.zeros((1, maxlen, nchars))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_indices[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, DIVERSITY)
        next_char = indices_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char

        sys.stdout.write(next_char)
        sys.stdout.flush()

print_callback = LambdaCallback(on_epoch_end=on_epoch_end)

model.fit(x, y, batch_size=128, epochs=281, callbacks=[print_callback], verbose=0)
