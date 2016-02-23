# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 14:59:22 2016

@author: davidruckes
"""
import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

ret = cap.set(3,640)   # Width of the frames in the video stream.
ret = cap.set(4,480)    # Height of the frames in the video stream.
ret = cap.set(5,15)     # Frame rate.
ret = cap.set(10,cap.get(10))    # Brightness of the image (only for cameras).
ret = cap.set(11,cap.get(11))    # Contrast of the image (only for cameras).
ret = cap.set(12,cap.get(12))    # Saturation of the image (only for cameras).
ret = cap.set(13,cap.get(13))    # Hue of the image (only for cameras).

fgbg = cv2.createBackgroundSubtractorMOG2()

kernel_open = np.ones((5,5),np.uint8)
kernel_close = np.ones((5,5),np.uint8)

rows = cap.get(3)
cols = cap.get(4)

while(cap.isOpened()):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel_open)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel_close)
    ret3,th3 = cv2.threshold(closing,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    cv2.imshow('thres',th3)
    cont_img = th3

    roi, contours, hierarchy = cv2.findContours(cont_img,cv2.RETR_TREE,
                                                cv2.CHAIN_APPROX_SIMPLE)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Found: ' + str(len(contours))
    cv2.putText(th3, text, (10, 20), font, 0.5,
                (255,255,255), 1, cv2.LINE_AA)

    if len(contours) > 0:
        cnt = contours[0]
        [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
        cv2.line(th3,(x-(100*vx),y-(100*vy)),(x,y),(0,255,0),2)
        #cv2.imshow('thres',th3)
        #time.sleep(0.1)
    #else:
        #cv2.imshow('thres',th3)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
