
import numpy as np

m = np.zeros(shape=(10, 10), dtype=np.uint8)
m[4, 5] = 1
m[5, 5] = 1
m[6, 5] = 1
m[5, 6] = 1
m[5, 7] = 1
m[5, 8] = 1

while True:
    print("\n".join(["".join(
        ["*" if cell else " " for cell in row]
        ) for row in m]))
    new = np.zeros(shape=(10, 10), dtype=np.uint8)
    new[:, 1:] += m[:, :-1] # right
    new[:, :-1] += m[:, 1:] # left
    new[1:, :] += m[:-1, :] # bottom
    new[:-1, :] += m[1:, :] # top
    new[1:, 1:] += m[:-1, :-1] # bottom right
    new[:-1, 1:] += m[1:, :-1]
    new[:-1, :-1] += m[1:, 1:]
    new[1:, :-1] += m[:-1, 1:]

    m[new < 2] = 0  # cells with too few neighbors die
    m[new > 3] = 0  # cells with too many neighbors die
    m[new == 3] = 1 # positions with 3 neighbors, a new cell is born
    input()
