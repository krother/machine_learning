
#
# 02 - functions on arrays
#
# take home message: NumPy makes loops go away

import numpy as np

# 1. create an array with 41 numbers from -10 .. +10
a = np.linspace(start=-10, stop=10, num=41)

# 2. calculate the sum of all numbers
a.sum()

# 3. round the numbers
a.round()

# 4. calculate the square of all numbers
a ** 2
np.pow(a, 2)
np.sum(np.pow(a, 2))  # chain functions

# 5. calculate the square root of all numbers
np.sqrt(a)
np.sqrt(a**2)  # same as:
np.abs(a)

# 6. calculate the logarithm of all numbers
np.log(a)
np.exp(a)

# 7. calculate trigonometric functions
np.sin(a)
b = np.linspace(start=0, stop=360, num=13)
np.sin(np.radians(b))
np.cos(np.radians(b)).round(2)
