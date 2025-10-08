#
# 05 - activation functions
#
# let's plot some activation functions

import numpy as np
from matplotlib import pyplot as plt

# 1. create some x data
x = np.linspace(start=-10, stop=10, num=101)

# 2. calculate a linear function (also an activation)
y = 3 * x + 4

# 3. create a line plot
plt.plot(x, y)
plt.show()

# 4. calculate a Rectified Linear Unit (ReLU)
y = x.copy()
y[y < 0] = 0   # select all positions where y is negative and set them to zero
plt.plot(x, y)
plt.show()

# 5. calculate a sigmoid function (logistic function)
y = 1 / (1 + np.exp(-x))

plt.plot(x, y)
plt.show()

# 6. create some random noise
y = np.random.normal(loc=5.0, scale=1.0, size=101)
plt.plot(x, y)
plt.show()
