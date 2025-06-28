
import numpy as np
"""
###
#..
"""
a = np.array([
[True, True, True],
[True, False, False]
])
a.astype(np.uint8)
a = a.astype(np.uint8)
box = np.zeros((12, 8), dtype=np.uint8)
box
a
box[4:6, 5:8] = a
box
box[4:6, 5:8] -= a
box[5:6, 5:8] -= a
box[5:7, 5:8] -= a
box
box[5:7, 5:8] = a
box
box[4:7, 5:8] + a
box[4:6, 5:8] + a
box
box
box[5:7, 5:8] -= a
box
box[6:8, 5:8] = a
box
box[:, 0] = 255
box[:, 0] = 10
box[:, -1] = 10
box[-1, :] = 10
box
box
a
a.transpose()
a.T
a
a
a[:, :]
x = np.arange(10)
x
x[::1]
x[::2]
x[::3]
x[::-1]
a
a[:, ::-1]
a[::-1, :]
a.T[:,::-1]
a = a.T[:,::-1]
a
a = a.T[:,::-1]
a
a = a.T[:,::-1]
a
import numpy as np
a = a.T[:,::-1]
a
np.argwhere(a)
coord = np.argwhere(a)
rot = np.array([[0, 1], [-1, 0]])
rot
coord.shape
# (4, 2) dot (2, 2) -> (4, 2)
coord
np.dot(coord, rot)
np.dot(coord, rot * -1)
rot
angle = 45
from math import sin, cos, radians
rad = radians(angle)
rad
rad*4
rot
rot45 = np.array([
   [cos(rad), sin(rad)],
   [-sin(rad), cos(rad)]])
rot45
np.dot(coord, rot45)
coord
for _ in range(8):
    coord = np.dot(coord, rot45)
coord