# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 10:14:07 2016

@author: davidruckes
"""

#Deformation Test
import numpy as np
import cv2
import time

# mouse callback function
def save_image(event,x,y,flags,param):
    global frame
    global i
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        text = 'caro_' + str(i) + '.jpg'
        print text
        cv2.imwrite(text,frame)
        i = i + 1

global frame
global i

cap = cv2.VideoCapture(1)
time.sleep(2)

#ret = cap.set(0,0)     # Current position of the video file in milliseconds.
#ret = cap.set(1,0)     # 0-based index of the frame to be decoded/captured next.
#ret = cap.set(2,0)     # Relative position of the video file
ret = cap.set(3,1600)   # Width of the frames in the video stream.
ret = cap.set(4,1200)    # Height of the frames in the video stream.
ret = cap.set(5,15)     # Frame rate.
#ret = cap.set(6,0)     # 4-character code of codec.
#ret = cap.set(7,0)     # Number of frames in the video file.
#ret = cap.set(8,0)     # Format of the Mat objects returned by retrieve() .
#ret = cap.set(9,0)     # Backend-specific value indicating the current capture mode.
ret = cap.set(10,cap.get(10))    # Brightness of the image (only for cameras).
ret = cap.set(11,cap.get(11))    # Contrast of the image (only for cameras).
ret = cap.set(12,cap.get(12))    # Saturation of the image (only for cameras).
ret = cap.set(13,cap.get(13))    # Hue of the image (only for cameras).
#ret = cap.set(14,0)    # Gain of the image (only for cameras).
#ret = cap.set(15,0)    # Exposure (only for cameras).
#ret = cap.set(16,0)    # Boolean flags indicating whether images should be converted to RGB.
#ret = cap.set(17,0)    # Currently unsupported
#ret = cap.set(18,0)    # Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)

for i in range(0,18):
    print str(i) + ': ' + str(cap.get(i))
i = 0
cv2.namedWindow('image')
cv2.setMouseCallback('image',save_image)

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    res = cv2.resize(frame,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('image',res)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()