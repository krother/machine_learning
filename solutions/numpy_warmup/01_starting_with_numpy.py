#
# 01 - Getting Started with NumPy
#
# execute in a Python shell or Jupyter
# no print() necessary
#

import numpy as np

# 1. create a Numpy array of numbers
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4], dtype=np.float32)
c = np.array([1, 2, 3, 4], dtype=np.uint8)

# 2. create an array with a range of integer numbers
a = np.arange(10)
b = np.arange(10, 20, dtype=np.int32)
c = np.arange(10000, dtype=np.float32)

# 3. create an array with a continuous range of floats
np.linspace(start=0, stop=5, num=11)
np.linspace(start=0, stop=10, num=101)

# 4. add 10 to each value of an array
a + 10

# 5. multiply each value in an array with a constant
a * 10

# 6. add two arrays position-wise
a + b

# 7. multiply two arrays position-wise
a * b
