import cv2

#read image
img = cv2.imread("fig/fig10.jpg")
#print size of image
 #(heigth, width, #chanels)... channels could be 3 (BGR)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#note that for gray scale no channels are sent
print("BGR image shape:")
print(img.shape) 
print("GrayScale image shape:")
print(imgGray.shape)
print("HSV image shape:")
print(imgHSV.shape)


#RESIZE FUNCTION:
imgResize = cv2.resize(img, (3024,4032))
cv2.imshow("Image",imgResize)
cv2.waitKey(0)

#CROPPING FUNCTION:
imgCrop = img[200:300,700:900]
cv2.imshow("Cropped Image", imgCrop)
cv2.waitKey(0)