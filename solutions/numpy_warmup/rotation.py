# simple 90° rotation
a = a.T[:,::-1]

import numpy as np
from math import sin, cos, radians

a = np.array([[1, 1, 1], [1, 0, 0]], dtype=np.uint8)
coord = np.argwhere(a)  # positions of nonzero values
rot = np.array([[0, 1], [-1, 0]])

# (4, 2) dot (2, 2) -> (4, 2)
np.dot(coord, rot)
np.dot(coord, rot * -1)

# rotate by angle other than 90°
angle = 45
rad = radians(angle)

rot45 = np.array([
   [cos(rad), sin(rad)],
   [-sin(rad), cos(rad)]
])

np.dot(coord, rot45)

for _ in range(8):
    coord = np.dot(coord, rot45)
