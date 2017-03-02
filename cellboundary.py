from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2

cap = cv2.VideoCapture('cells.webm')
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter('output1.avi',fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()

    
    ret, frame = cap.read()

    if ret == True:
        

        element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
        frame = cv2.blur(frame,(15,15))
        frame = cv2.blur(frame,(15,15))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        erosion1 = cv2.erode(gray,element,iterations = 1)
        dilation1 = cv2.dilate(erosion1,element,iterations=1)
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        blur = cv2.bilateralFilter(dilation1,5,75,75)
        lower_blue = np.array([130,50,50])
        upper_blue = np.array([200,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        res_blue = cv2.bitwise_and(frame,frame, mask= mask)
        res_blue_gray = cv2.cvtColor(res_blue,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(dilation1,(5,5),0)
        ret3,th3 = cv2.threshold(dilation1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        erosion = cv2.erode(res_blue_gray,element,iterations = 1)
        dilation = cv2.dilate(erosion,element,iterations=1)

        image, contours, hierarchy = cv2.findContours(dilation.copy(), \
                               cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        dilation = cv2.cvtColor(dilation,cv2.COLOR_GRAY2RGB)
        dilation = cv2.drawContours(dilation, contours, -1, (0,255,0), 3)
        
        cv2.imshow('frame',dilation)
        #out.write(res_blue_gray)

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
