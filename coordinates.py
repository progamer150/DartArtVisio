# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 10:14:07 2016

@author: davidruckes
"""

#Deformation Test
import numpy as np
import cv2
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global i
    global punkte
    if event == cv2.EVENT_LBUTTONDBLCLK:
        draw_overlay[:] = 0
        cv2.circle(draw_overlay,(x,y),1,(0,0,255),2)
        ret, mask = cv2.threshold(draw_overlay, 10, 255, cv2.THRESH_BINARY)
        img2gray = cv2.cvtColor(draw_overlay,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        rows,cols,channels = img.shape
        roi = img[0:rows, 0:cols ]
        img_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        dst = cv2.add(img_bg,draw_overlay)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'X: ' + str(x) + ' Y: ' + str(y) + '   Press Escape to close the Window!'
        cv2.putText(dst, text, (10, 20), font, 0.5,
                    (0,0,0), 1, cv2.LINE_AA)
        cv2.imshow('image',dst)
        
        punkte[i,0] = x
        punkte[i,1] = y
        
        i = i + 1
        print
        print punkte
        
        if i>3:
            i = 0
            deform()
        
def deform():
    global punkte
    pts2 = np.float32([[50,50],[150,50],[150,150],[50,150]])
    M = cv2.getPerspectiveTransform(punkte,pts2)
    
    dst = cv2.warpPerspective(img,M,(200,200))
    
    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')
    plt.show()

img = cv2.imread('ring.jpg')
rows,cols,channels = img.shape

global i
i = 0

global punkte
punkte = np.float32([[0,0],[0,0],[0,0],[0,0]])

draw_overlay = np.zeros((rows,cols,3), np.uint8)
draw_overlay[0:rows, 0:cols]
draw_overlay[:] = 0
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

cv2.imshow('image',img)

while(1):
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()