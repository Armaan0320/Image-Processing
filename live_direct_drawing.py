import cv2
import numpy as np


'''live direct drawing, for example drawing any shape
with a single or double click of your mouse or any keyboard key.'''

def draw(event, x, y, flags, params):
    # print("Event triggered")
    # print(event)
    # if event == 0:
    #     print("Mouse moved")
    # elif event == 1:
    #     print("Mouse down clicked")
    # elif event == 4:
    #     print("Mouse key released.")

    if event ==1:
        cv2.circle(img, center=(x,y), radius = 50, color =(0,0,255),thickness =-1)



cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", draw)

img = np.zeros((512,512,3))

while True: #creates an infinite loop
    cv2.imshow("window", img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break #pressing of keyboard key 'x' breaks the loop.

cv2.destroyAllWindows()