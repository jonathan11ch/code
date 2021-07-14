import cv2
import numpy as np

#define colors
BLUE  = (255,0,0)
GREEN = (0,255,0)
RED  = (0,0,255) 

img = cv2.imread("fig/fig8.jpg")
print(img.shape)



#define the four corner points
width  = 3500
height = 2500
pts1 = np.float32([[179,611],[179,2650],[2926,10],[2815,3278]])
pts2 = np.float32([[0,0],[0,height],[width,0],[width, height]])


matrix  = cv2.getPerspectiveTransform(pts1,pts2)
output = cv2.warpPerspective(img,matrix,(width,height))


cv2.line(img, [179,611],[0,0],RED,4)
cv2.line(img, [179,2650],[0,0],RED,4)
cv2.line(img, [2926,10],[0,0],RED,4)
cv2.line(img, [2815,3278],[0,0],RED,4)

cv2.imshow("Image", img)
cv2.waitKey(0)

cv2.imshow("Image warpPerspective", output)
cv2.waitKey(0)