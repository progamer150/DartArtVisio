# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 09:30:13 2016

@author: davidruckes
"""
import numpy as np
import cv2

img = cv2.imread('dart.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
roi, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

if len(contours) < 2:
    cnt = contours[0]
else:
    cnt = contours[2]


rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
print vx
print vy
print x
print y

if False:
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
else:
    cv2.line(img,(x-(100*vx),y-(100*vy)),(x,y),(0,255,0),2)




cv2.imshow('find_line',img)
cv2.waitKey(0)