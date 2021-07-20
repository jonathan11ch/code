import cv2

faceCascade = cv2.CascadeClassifier("files/haarcascade_frontalface_default.xml")
img  = cv2.imread('fig/fig16.jpg')
imgGray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.2, 3)

thick = 2
color = (255,0,0)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), color,thick)


cv2.imshow("image", img)
cv2.waitKey(0)
