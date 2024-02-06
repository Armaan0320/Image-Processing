import cv2
import numpy as np

#Reading an image


img = np.zeros((512,512,3)) #a complete black image

#creating a rectangle
# cv2.rectangle(img, pt1=(100,100), pt2=(300,300), color=(255,0,0), thickness = 3)
cv2.rectangle(img, pt1=(100,100), pt2=(300,300), color=(255,0,0), thickness = -1)






cv2.imshow("window",img)
cv2.waitKey(0)
