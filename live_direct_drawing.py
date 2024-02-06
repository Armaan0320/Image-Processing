import cv2
import numpy as np

img = np.zeros(((512,512,3)))

'''live direct drawing, for example drawing any shape
with a single or double click of your mouse or any keyboard key.'''

while True: #creates an infinite loop
    cv2.imshow("window", img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break #pressing of keyboard key 'x' breaks the loop.

cv2.destroyAllWindows()