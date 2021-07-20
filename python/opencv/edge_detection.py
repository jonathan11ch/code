import cv2
import numpy as np


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area > 50:
            perimeter = cv2.arcLength(cnt, True)
            #print(perimeter)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            print(len(approx))
            if len(approx) == 12:
                objectType = "Hex"
                cv2.drawContours(imgContour, cnt, -1,(0,255,0),6)
                x,y,w,h = cv2.boundingRect(approx)
                cv2.rectangle(imgContour, (x,y),(x+w,y+h),(0,0,255),4)
                cv2.putText(imgContour,objectType,(x+(w//2)-10, y+(h//2 -10)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)




img     = cv2.imread("fig/shapes.jpg")
img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))


imgGray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur  = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgContour = img.copy()
getContours(imgCanny)

#stack images
imgBlank = np.zeros_like(imgGray)
imgStack1 = np.hstack((imgBlur,imgGray))
imgstack2 = np.hstack((imgCanny,imgBlank))

imgStack =  np.vstack((imgStack1,imgstack2))

cv2.imshow("figure", imgStack)
cv2.imshow("figure2", imgContour)
cv2.waitKey(0)
