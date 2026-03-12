
import numpy as np
from PIL import Image


for name in ["tram", "monkey"]: 

    im = Image.open(f'{name}_resized.png')
    assert im.size == (224, 224)

    a = np.array(im)
    print(a.shape, a.dtype)

    # flip left-right
    b = a[:, ::-1]
    Image.fromarray(b).save(f"{name}_left_right.png")

    # upside-down
    b = a[::-1]
    Image.fromarray(b).save(f"{name}_upside_down.png")

    # remove every 2nd column
    b = a.copy()
    b[:,::2] = 0
    Image.fromarray(b).save(f"{name}_stripes.png")

    # swap upper + lower half
    b = a.copy()
    b[:112] = a[112:]
    b[112:] = a[:112]
    Image.fromarray(b).save(f"{name}_swap.png")

    # make it brighter
    b = a.astype(np.int16) + 150
    b[b > 255] = 255
    b = b.astype(np.uint8)
    Image.fromarray(b).save(f"{name}_bright.png")

    # make it darker
    b = a.astype(np.int16) - 150
    b[b < 0] = 0
    b = b.astype(np.uint8)
    Image.fromarray(b).save(f"{name}_dark.png")

    # black spot in the middle
    b = a.copy()
    b[65:175, 65:175] = 0
    Image.fromarray(b).save(f"{name}_hole.png")

    im2 = im.rotate(135)
    im2.save(f"{name}_rotate.png")


im1 = Image.open(f'tram_resized.png')
im2 = Image.open(f'monkey_resized.png')
a = np.array(im1).astype(np.int16)
b = np.array(im2).astype(np.int16)
c = ((a + b) // 2).astype(np.uint8)
Image.fromarray(c).save(f"blend.png")
