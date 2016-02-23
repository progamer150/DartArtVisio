# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 10:14:07 2016

@author: davidruckes
"""

#Deformation Test
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('start.jpg')

pts1 = np.float32([[144,232],[489,232],[634,283],[6,282]])
pts2 = np.float32([[17,82],[284,112],[256,277],[43,256]])

M = cv2.getPerspectiveTransform(pts1,pts2)
print M
dst = cv2.warpPerspective(img,M,(340,340))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

