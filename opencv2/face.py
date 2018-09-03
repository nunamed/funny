import cv2
import numpy as np
#我把opencv2安装在d盘
face_classfier = cv2.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
eye_classfier = cv2.CascadeClassifier(r'D:/opencv/sources/data/haarcascades/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while True:
	ret,frame=cap.read()
	frame = cv2.flip(frame,1)
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	image = cv2.equalizeHist(gray)
	faces = face_classfier.detectMultiScale(image,1.1,5,cv2.CASCADE_SCALE_IMAGE)
	eyes = eye_classfier.detectMultiScale(image,1.2,4,cv2.CASCADE_SCALE_IMAGE)
	if len(eyes):
		for x,y,w,h in eyes:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
	if len(faces):
		for x,y,w,h in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
	cv2.imshow('test',frame)
	if cv2.waitKey(1)&0xFF==ord('q'):
		break
cv2.destroyAllWindows()