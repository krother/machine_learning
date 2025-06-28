"""
manage Tetris environment with NumPy
"""
import numpy as np

# create a brick
a = np.array([
    [True, True, True],
    [True, False, False]
])
a = a.astype(np.uint8)

box = np.zeros((12, 8), dtype=np.uint8)
# add block to box
box[4:6, 5:8] = a

# remove block
box[4:6, 5:8] -= a

# place block one row lower
box[5:6, 5:8] -= a

# create border
box[:, 0] = 10
box[:, -1] = 10
box[-1, :] = 10
