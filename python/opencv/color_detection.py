import cv2
import numpy as np
import time
def createTrackBarWindow():
	#create empty window
	cv2.namedWindow("TrackBars")
	#resize window
	cv2.resizeWindow("TrackBars",540,240)
	#create sliders to set Hue, Saturation, Value
	cv2.createTrackbar("Hue min","TrackBars", 0  ,179,onChange)
	cv2.createTrackbar("Hue max","TrackBars", 179,179,onChange)
	cv2.createTrackbar("Sat min","TrackBars", 0  ,255,onChange)
	cv2.createTrackbar("Sat max","TrackBars", 255,255,onChange)
	cv2.createTrackbar("Val min","TrackBars", 0  ,255,onChange)
	cv2.createTrackbar("Val max","TrackBars", 255,255,onChange)


def onChange(a):
	pass

def getTrackbarValues():
	hue_min = cv2.getTrackbarPos("Hue min","TrackBars")
	hue_max = cv2.getTrackbarPos("Hue max","TrackBars")
	sat_min = cv2.getTrackbarPos("Sat min","TrackBars")
	sat_max = cv2.getTrackbarPos("Sat max","TrackBars")
	val_min = cv2.getTrackbarPos("Val min","TrackBars")
	val_max = cv2.getTrackbarPos("Val max","TrackBars")
	return [hue_min,hue_max,sat_min,sat_max,val_min,val_max]

def main():
	#load image
	img =  cv2.imread("fig/fig8.jpg")
	img = cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))
	#create trackbar
	createTrackBarWindow()
	#convert to HSV color space
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	#show image
	while True:

		[hue_min,hue_max,sat_min,sat_max,val_min,val_max] = getTrackbarValues()
		#set color bounds
		lower = np.array([hue_min,sat_min,val_min])
		upper = np.array([hue_max,sat_max,val_max])
		#create mask
		mask  = cv2.inRange(imgHSV,lower,upper)
		#apply mask to the original image (AND) operation
		imgResult = cv2.bitwise_and(img, img, mask=mask)
		#show image
		cv2.imshow("image HSV", imgResult)
		cv2.waitKey(100)


main()
