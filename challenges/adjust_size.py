
from PIL import Image
import sys
import os

path = sys.argv[1]

for fn in os.listdir(path):
    im = Image.open(os.path.join(path, fn))
    xsize, ysize = im.size
    print(fn, im.size)

    if xsize <= ysize:
        margin = (ysize - xsize) // 2
        im = im.crop((0, margin, xsize - 1, margin + xsize - 1))

    else:
        margin = (xsize - ysize) // 2
        im = im.crop((margin, 0, margin + ysize - 1, ysize - 1))
    print(im.size)

    im.save(path + os.sep + "cropped_" + fn)
    im = im.resize((224, 224))
    im.save(path + os.sep + "resized_" + fn)
