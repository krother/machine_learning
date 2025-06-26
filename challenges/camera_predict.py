"""
Collect image data from your camera
and save them to files
(224 x 224 x 3)

pip install opencv-python
"""
import numpy as np
import pickle
import cv2

# frame size = 480, 640
YSTART = 16
XSTART = 96

GREEN = np.array([0, 255, 0])

cap = cv2.VideoCapture(0)

#m = pickle.load(open("model.pkl", "rb"))

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

        # predict
        a = inner[::2, ::2]
        print(a.shape)
        ...  # prediction goes here


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
