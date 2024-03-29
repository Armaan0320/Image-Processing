import cv2
import numpy as np
 
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
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(img_gray.shape)

#cv2.imshow("window", img)
#cv2.imshow("window", img_gray)

# #showing yellowish tint
# blue = img[:,:,0] #basically its a 3d numpy array and we zeroed out the blue channel completely

# green = img[:,:,1] #we zeroed out the green  channel completely - purple shade

# red = img[:,:,2] #we zeroed out the red  channel completely - aqua type shade

# new_img = np.hstack((blue, green, red))

# cv2.imshow("window", new_img)

# img_resize = cv2.resize(img, (800,800))
# img_resize = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))

# cv2.imshow("window", img_resize)

#flipping an image
#flipping an image on x axis
# img_flip = cv2.flip(img, 0)

#flipping an image on y axis  
# img_flip = cv2.flip(img, 1)


# flipping an image vertically and horizontally
img_flip = cv2.flip(img, -1)

cv2.imshow("window", img_flip)


cv2.waitKey(0)