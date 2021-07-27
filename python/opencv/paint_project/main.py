import cv2
import numpy as np

def filterGreenColor(frameHSV):
    #set the color thresholds
    lower_green = np.array([34, 98, 181])
    upper_green = np.array([60, 164, 255])
    #extract the mask
    return cv2.inRange(frameHSV, lower_green, upper_green)


def getTipPointer(mask, threshold = 1):
    #detect edges
    maskCany = cv2.Canny(mask,50,50)
    #find contours
    contours,hierarchy = cv2.findContours(maskCany,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    if contours:
        #obtain contour of max area
        c = max(contours, key= cv2.contourArea)
        #extract features
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02*perimeter, True)
        #filter contour
        if area > threshold and len(approx) > 2:
            #print(area)
            x,y,w,h = cv2.boundingRect(approx)
            center = (x+w//2,y)
            radius = 5
            GREEN = (0,255,0)
            #draw circle
            cv2.circle(paintImg, center,radius,GREEN,cv2.FILLED)

    return maskCany

print("aa")
'''
TODO:
0. Open the webcam
1. Define Marker color (define the mask)
2. Locate the tip of the marker ()
3. Draw (filled) a circle with given coordinates
'''
#COLOR RANGES FOR FILER
#GREEN: min[34, 98, 181] max[60, 164, 255]



videoWebcam = cv2.VideoCapture(0)
videoWebcam.set(3, 640) #height
videoWebcam.set(4, 480) #width
videoWebcam.set(10,10) #brigthness
paintImg = np.zeros((480,640,3), np.uint8)

while not(cv2.waitKey(10) & 0xFF == ord('q')):
    #print("while")
    success, frame = videoWebcam.read()
    #convert img to grayscale
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #filter color
    mask_green = filterGreenColor(frameHSV)
    #extract edges
    maskCany = getTipPointer(mask_green, 5)
    #add painted image with current frame
    framePaint = cv2.add(frame, paintImg)
    #stack images
    imgStack = np.hstack((mask_green,maskCany))
    #display images
    cv2.imshow("stack Image", imgStack)
    cv2.imshow("paint image", framePaint)
