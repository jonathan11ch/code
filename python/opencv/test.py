import cv2
import time

print("Loading Image Example")

#load single image
img =  cv2.imread("fig/fig1.jpg")
#show image in a window
cv2.imshow("Output", img)
#wait until any key is pressed on the image
key = cv2.waitKey(0)
print(bin(key))
#close all windows
cv2.destroyAllWindows()
print("Finished Process")

print("Loading Video Example")

#load video
videoCapture = cv2.VideoCapture("fig/video.mp4")

while not(cv2.waitKey(100) & 0xFF == ord('q')):
	#read frame from video
	success, frame = videoCapture.read()
	#show the frame in window
	cv2.imshow("Output Video", frame)

print("Finished Process")


print("Webcam Video Access")

#open webcam with id=0
videoCapture = cv2.VideoCapture(0)
videoCapture.set(3, 640) #id = 3: height
videoCapture.set(4, 480) #id = 4: width
videoCapture.set(10, 100) #id=10, brigthness


while not(cv2.waitKey(1) & 0xFF == ord('q')):
	#read frame from video
	success, frame = videoCapture.read()
	#show the frame in window
	cv2.imshow("Output Video", frame)

print("Finished Process")
