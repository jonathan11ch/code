import cv2
import numpy as np 

#define colors
BLUE  = (255,0,0)
GREEN = (0,255,0)
RED  = (0,0,255) 
#create empty image matrix
img = np.zeros((512,512,3), np.uint8)

print(img.shape)
img[:] = BLUE

#DRAW A LINE
start = (0,0)
end   = (300,300)
thickness = 2
cv2.line(img, start,end,GREEN,thickness)

#DRAW A RECTANGLE
start = (0,0)
end   = (200,120)
thickness = 3
cv2.rectangle(img, start,end,RED, cv2.FILLED)

#DRAW A CIRCLE
center = (350,350)
radius = 50
thickness = 5
cv2.circle(img, center,radius,GREEN,thickness)

#WRITE TEXT
text = "JONATHAN"
origin = (10, 400)
scale = 1
thickness = 1
cv2.putText(img, text, origin, cv2.FONT_HERSHEY_COMPLEX, scale, RED,thickness)

#Show image
cv2.imshow("Image", img)
cv2.waitKey(0)


