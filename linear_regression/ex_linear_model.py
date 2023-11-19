from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pylab as plt

X, y = mglearn.datasets.make_wave(n_samples=60)

Xtrain, Xtest, ytrain, ytest = train_test_split(
            X, y,
            random_state=42)

lr = LinearRegression().fit(Xtrain, ytrain)

print("Coefficients:", lr.coef_)
print("Intercept   :", lr.intercept_)

print("train score :", lr.score(Xtrain, ytrain))
print("test score  :", lr.score(Xtest, ytest))


# plot the result
Xideal = np.linspace(-3.0, 3.0, 100)
yideal = lr.coef_[0] * Xideal + lr.intercept_

plt.figure()
plt.plot(Xtrain, ytrain, 'bs', label="train")
plt.plot(Xtest, ytest, 'ro', label="test")
plt.plot(Xideal, yideal, 'k-', label="fitted")
plt.legend()