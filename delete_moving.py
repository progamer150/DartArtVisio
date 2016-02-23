# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 14:59:22 2016

@author: davidruckes
"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

ret = cap.set(3,640)   # Width of the frames in the video stream.
ret = cap.set(4,480)    # Height of the frames in the video stream.
ret = cap.set(5,15)     # Frame rate.
ret = cap.set(10,cap.get(10))    # Brightness of the image (only for cameras).
ret = cap.set(11,cap.get(11))    # Contrast of the image (only for cameras).
ret = cap.set(12,cap.get(12))    # Saturation of the image (only for cameras).
ret = cap.set(13,cap.get(13))    # Hue of the image (only for cameras).

fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg.setDetectShadows(False)    # Disable detecting shadows
print fgbg.getHistory()
#fgbg.setHistory(20)
print fgbg.getNMixtures()
#fgbg.setNMixtures(5)
print fgbg.getBackgroundRatio()
#fgbg.setBackgroundRatio(0.5)
print fgbg.getComplexityReductionThreshold()
#fgbg.setComplexityReductionThreshold(0.001)
print fgbg.getVarThreshold()
#fgbg.setVarThreshold(50)




kernel_open = np.ones((5,5),np.uint8)
kernel_close = np.ones((5,5),np.uint8)

while(cap.isOpened()):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    #res = cv2.resize(fgmask,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)

#    img2_fg = cv2.bitwise_and(frame,frame,mask = fgmask)
    cv2.imshow('mask',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
