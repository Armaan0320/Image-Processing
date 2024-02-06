import cv2
import numpy as np

Img = cv2.imread("img/aripnlane.png")
img_crop = Img[100:300,200:500]

# cropping from origin
# img_crop = Img[0:30,0:50]
 
cv2.imwrite("cropped_airplane.png", img_crop)
cv2.imshow("window", img_crop)
cv2.waitKey(0)