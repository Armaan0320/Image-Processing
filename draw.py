import cv2
import numpy as np

#Reading an image


img = np.zeros((512,512,3)) #a complete black image

#creating a rectangle
# cv2.rectangle(img, pt1=(100,100), pt2=(300,300), color=(255,0,0), thickness = 3)
cv2.rectangle(img, pt1=(100,100), pt2=(300,300), color=(255,0,0), thickness = -1 )

#creating a circle
cv2.circle(img, center =(100,400), radius=70, color=(0,0,225), thickness = -1)

#drawing a line
cv2.line(img, pt1=(0,0), pt2=(512,512), thickness =2, color = (0,255,0))

#adding text
cv2.putText(img, org=(10,200), fontScale=1,color=(0,255,255), thickness =2, lineType=cv2.LINE_AA, text="Hey, How you doin?", fontFace=cv2.FONT_ITALIC )


cv2.imshow("window",img)
cv2.waitKey(0)

