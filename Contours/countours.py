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
        
        frame1=frame
        kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
        kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                             [-1,2,2,2,-1],
                             [-1,2,8,2,-1],
                             [-1,2,2,2,-1],
                             [-1,-1,-1,-1,-1]]) / 8.0
        frame = cv2.filter2D(frame, -1, kernel_sharpen_3)
      
        element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))

        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        x = frame.shape[0]
        y = frame.shape[1]
        hsvt = hsv[x/3:(2*x)/3,y/3:(2*y)/3,:]
        target = cv2.cvtColor(hsvt,cv2.COLOR_HSV2BGR)
        #cv2.imshow('i',hsv[:,:,:])
        hsv = cv2.GaussianBlur(hsv,(5,5),0)
        roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
    
      # normalize histogram and apply backprojection
        cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
        dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
   
      # Now convolute with circular disc
        disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
        cv2.filter2D(dst,-1,disc,dst)
    
      # threshold and binary AND
        ret,thresh = cv2.threshold(dst,50,255,0)
        thresh = cv2.merge((thresh,thresh,thresh))
        res = cv2.bitwise_and(target,thresh)
        #cv2.imshow('res',res)
        frame = cv2.filter2D(frame, -1, kernel_sharpen_3)
        c = 2.5
        hsv = hsv*c
        lower_blue = np.array([130*c,50*c,50*c])
        upper_blue = np.array([200*c,255*c,255*c])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        res_blue = cv2.bitwise_and(frame,frame, mask= mask)
        res_blue_gray = cv2.cvtColor(res_blue,cv2.COLOR_BGR2GRAY)

        x = frame.shape[0]
        y = frame.shape[1]
        
        erosion = cv2.erode(res_blue_gray,element,iterations = 1)
        dilation = cv2.dilate(erosion,element,iterations=1)
        
        
        image, contours, hierarchy = cv2.findContours(dilation.copy(), \
                               cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
       
        dilation = cv2.cvtColor(dilation,cv2.COLOR_GRAY2RGB)
        dilation = cv2.drawContours(frame1, contours, -1, (0,255,0), 3)
        
       
        cv2.imshow('frame',dilation)
        #out.write(res_blue_gray)

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
