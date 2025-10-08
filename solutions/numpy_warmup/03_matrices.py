#
# 03 - reshaping and matrices
#

import numpy as np

# 1. create an array with 6 numbers 
a = np.array([1, 2, 3, 4, 5, 6])

# 2. create a column vector with 6 numbers
b = np.array([[1], [2], [3], [4], [5], [6]])

# 3. create a 2 x 3 matrix
c = np.array([[1, 2, 3], [4, 5, 6]])
c = a.reshape((2, 3))
c = b.reshape((2, 3))

# 4. create a 3 x 2 matrix
d = a.reshape((3, 2))
d = b.reshape((3, 2))
d = c.reshape((3, 2))
d = c.transpose()

# 5. multiply an array with a column vector
a * b

# 6. create a 10x10 matrix with numbers 1..100
m = np.arange(100).reshape(10, 10)

# 7. remove all numbers divisible by 7
m[m % 7 == 0] = 0

# 8. create a random matrix of dice rolls
n = np.random.randint(1, 7, size=(5, 5))  # 7 is not included
