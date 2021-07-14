import cv2
import numpy as np 

#read image
img = cv2.imread("fig/fig16.jpg")

#STACK IMAGES TOGETHER
imgHor = np.hstack((img, img))

imgVer = np.vstack((imgHor,imgHor))

#TODO: code stackImages function to stack an array of images
#imgStack = np.stackImages(0.5, ([img,img,img],[img,img,img]))

cv2.imshow("Stack", imgHor)
cv2.waitKey(0)
cv2.imshow("Stack", imgVer)
cv2.waitKey(0)
cv2.imshow("Stack", imgStack)
cv2.waitKey(0)