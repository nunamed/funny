import cv2
cap = cv2.VideoCapture(r'C:\Users\admin\Desktop\a.avi')
while (cap.isOpened()):
	ret,frame = cap.read()
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()