import numpy as np
from matplotlib import pyplot as plt

# rectified linear unit (ReLU)
x = np.linspace(-5, +5, 100)
y = x.copy()
y[y < 0] = 0   # select all positions where y is negative and set them to zero

plt.plot(x, y)
# plt.show()
plt.figure()

# sigmoid function (logistic function)
x = np.linspace(-5, +5, 100)
y = 1 / (1 + np.exp(-x))

plt.plot(x, y)
plt.show()
