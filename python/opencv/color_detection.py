import cv2
import numpy as np
import time
def createTrackBarWindow():
	#create empty window
	cv2.namedWindow("TrackBars")
	#resize window
	cv2.resizeWindow("TrackBars",1200,240)
	#create sliders to set Hue, Saturation, Value
	cv2.createTrackbar("Hue min","TrackBars", 0  ,179,onChange)
	cv2.createTrackbar("Hue max","TrackBars", 179,179,onChange)
	cv2.createTrackbar("Sat min","TrackBars", 0  ,255,onChange)
	cv2.createTrackbar("Sat max","TrackBars", 255,255,onChange)
	cv2.createTrackbar("Val min","TrackBars", 0  ,255,onChange)
	cv2.createTrackbar("Val max","TrackBars", 255,255,onChange)


def onChange(a):
	pass


def main():
	#load image
	img =  cv2.imread("fig/fig7.jpg")

	#create trackbar
	createTrackBarWindow()
	#convert to HSV color space
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	#show image
	while True:
		hue_min = cv2.getTrackbarPos("Hue min","TrackBars")
		#cv2.imshow("image", img)
		cv2.imshow("image HSV", imgHSV)
		print(hue_min)
		cv2.waitKey(100)

	

main()

