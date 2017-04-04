import cv2
import numpy as np

cap = cv2.VideoCapture('cells.avi')

while(cap.isOpened()):
	ret,frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower_purple = np.array([130,50,140])
	upper_purple = np.array([170,255,255])
	mask = cv2.inRange(hsv, lower_purple, upper_purple)
	res = cv2.bitwise_and(frame,frame, mask= mask)
	blur = cv2.GaussianBlur(res,(7,7),0)
	kernel = np.ones((5,5),np.uint8)
	dilation = cv2.dilate(blur,kernel,iterations = 1)
	edges = cv2.Canny(dilation,100,200)
	cv2.imshow('edges',edges)
	#cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()	
