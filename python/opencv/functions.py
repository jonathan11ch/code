import cv2
import numpy as np

img = cv2.imread("fig/fig11.jpg")

#color space convertions
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgHSV  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#blur function  GaussianBlur(img, kerlnel[], sigma)
# the kernel should be defined with size of ODD numbers
#sigmax and sigmay denot the standard deviations
imgBlur = cv2.GaussianBlur(imgGray, (21,21), 0)

#edge detector with thresholds 100 and 100
imgCanny = cv2.Canny(img, 150, 150)

#define kernel for dilation
kernel = np.ones((5,5),np.uint8)
#image dialation
imgDilation =cv2.dilate(imgCanny, kernel, iterations = 1)

#erode function
imgErode = cv2.erode(imgDilation, kernel, iterations =1)


cv2.imshow("grayscale", imgGray)
cv2.waitKey(0)

cv2.imshow("HSV color space", imgHSV)
cv2.waitKey(0)

cv2.imshow("blur grayscale", imgBlur)
cv2.waitKey(0)

cv2.imshow("edge detector", imgCanny)
cv2.waitKey(0)

cv2.imshow("edge Dialation", imgDilation)
cv2.waitKey(0)

cv2.imshow("edge erode", imgErode)
cv2.waitKey(0)