"""
Fashion MNIST
https://github.com/zalandoresearch/fashion-mnist
"""
from mnist_reader import load_mnist
from matplotlib import pyplot as plt
import numpy as np


CLASSES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

data, labels = load_mnist(".")

im = data[3].reshape(28, 28)

plt.imshow(im, cmap='Greys')


# Train a Logistic Regression model

# input training data: pixel information for all images
Xtrain = data[:20000].astype(np.float32) / 255.0  # normalize (scale) to 0..1

# ouput training data: labels
# 1: T-shirt;  0: not T-shirt
ytrain = (labels[:20000] == 0).astype(int)

# hyperparameters: learning rate, portion of training data used
# fitting algorithm: gradient descent

# create random parameter vector of 784
n_params = Xtrain.shape[1]
np.random.seed(42)
a = np.random.random(size=n_params) - 0.5
a.shape

# model: sigmoid function
def sigmoid(X, a):
    return 1 / (1 + np.exp(-np.dot(X, a)))

def logloss(X, ytrue, a):
    yhat = sigmoid(X, a)
    n = X.shape[0]
    return -1/n * sum(
        ytrue * np.log(yhat) +
        (1-ytrue) * np.log(1-yhat) / 9.0
    )


loss = logloss(Xtrain, ytrain, a)


# gradient descent for logistic regression
iteration = 0
loss_data = []
learning_rate = 0.1

while iteration < 100:
    # calculate loss for modified a -> gradient
    epsilon = 0.001
    gradient = []
    for i in range(n_params):
        a_mod = a.copy()
        a_mod[i] += epsilon
        loss_mod = logloss(Xtrain, ytrain, a_mod)
        gradient.append((loss_mod - loss) / epsilon)

    gradient = np.array(gradient)

    # calculate new a
    a = a - gradient * learning_rate

    loss = logloss(Xtrain, ytrain, a)
    loss_data.append(loss)

    iteration += 1
    print(f"iteration: {iteration:5}    log-loss: {loss:20.6f}")


from matplotlib import pyplot as plt

plt.plot(loss_data)
plt.show()

ytrain[:10]

# ### calculate metrics for the training data
predictions = sigmoid(Xtrain, a).round()

n = ytrain.shape
correct = np.abs(predictions - ytrain)
accuracy = (n - sum(correct)) / n
accuracy[0]


### evaluate metrics for test data
Xtest = data[50000:].astype(np.float32) / 255.0  # normalize (scale) to 0..1
ytest = (labels[50000:] == 0).astype(int)

predictions = sigmoid(Xtest, a).round()

n = ytest.shape
correct = np.abs(predictions - ytest)
accuracy = (n - sum(correct)) / n
accuracy[0]

# false positive: we predict T-shirt but it is something else
FP = sum((predictions - ytest) == +1)

# false negative: we predict something else but it is a t-shirt
FN = sum((predictions - ytest) == -1)

# true positive: we predict t-shirt and it is one
TP = sum((predictions + ytest) == 2)

# true negative: we predict not-t-shirt and it is correct
TN = sum((predictions + ytest) == 0)


FP, FN, TP, TN
