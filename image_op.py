import cv2
import numpy as np

img = cv2.imread("img/fruits.png")
cv2.imshow("res", img)

#now trying the .split function
#split - return 3 channel of your image
b, g, r = cv2.split(img)
cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)
cv2.imshow("original", img)



cv2.waitKey(0)
cv2.destroyAllWindows()