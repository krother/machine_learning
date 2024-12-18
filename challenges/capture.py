"""
Collect image data from your camera
and save them to files
(224 x 224 x 3)
"""
import numpy as np
import cv2
from PIL import Image

# frame size = 480, 640
YSTART = 16
XSTART = 96

GREEN = np.array([0, 255, 0])

cap = cv2.VideoCapture(0)

i = 1
while(True):
    ret, frame = cap.read()

    # draw a green rectangle
    inner = frame[YSTART:YSTART+448, XSTART:XSTART+448].copy()
    frame[YSTART-2:YSTART+448+2, XSTART-2:XSTART+448+2] = GREEN
    frame[YSTART:YSTART+448, XSTART:XSTART+448] = inner
    # Display the resulting frame
    cv2.imshow('frame', frame)

    # save image if you press space
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord(' '):
        # swap color channels
        a = inner[:,:,0].copy()
        b = inner[:,:,1].copy()
        c = inner[:,:,2].copy()
        inner[:,:,0] = c
        inner[:,:,1] = b
        inner[:,:,2] = a

        # write image
        im = Image.fromarray(inner)
        im = im.resize((224, 224))
        im.save(f'out{i:04d}.png')
        i += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
