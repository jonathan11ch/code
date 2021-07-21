import cv2
import numpy as np

def filterGreenColor(frameHSV):
    lower_green = np.array([34, 98, 181])
    upper_green = np.array([60, 164, 255])

    mask_green = cv2.inRange(frameHSV, lower_green, upper_green)
    return mask_green

def getTipPointer(mask, threshold):
    maskCany = cv2.Canny(mask,50,50)
    contours,hierarchy = cv2.findContours(maskCany,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    list = [cv2.contourArea(c) for c in contours]
    if list:
        index = list.index(max(list))
        c = contours[index]
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02*perimeter, True)
        if area > threshold and len(approx) > 2:
            #print(area)
            x,y,w,h = cv2.boundingRect(approx)
            center = (x,y)
            radius = 20
            GREEN = (0,255,0)
            cv2.circle(paintImg, center,radius,GREEN,cv2.FILLED)
            #cv2.drawContours(paintImg, c, -1, (255,0,0),3)


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
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    print(frame.shape)
    print(paintImg.shape)
    mask_green = filterGreenColor(frameHSV)
    maskCany = getTipPointer(mask_green, 5)
    cv2.imshow("webcam", cv2.add(frame, paintImg))
    cv2.imshow("mask", mask_green)
    cv2.imshow("tip", maskCany)
