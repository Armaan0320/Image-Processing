import cv2
import numpy
 
#reading an image
img = cv2.imread("img/fruits.png")
'''
#to show the type of image - that is - numpy array
print(type(img))

#to show the shape of the image
print(img.shape)

#to know the size fo the image
print(img.size)
'''
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)

#cv2.imshow("window", img)
cv2.imshow("window", img_gray)
cv2.waitKey(0)