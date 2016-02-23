import numpy as np
import cv2
import math

def draw_angle_line(img, xpos, ypos, inner, outer, angle, red, green,
                    blue, strength):
    angle = math.radians(angle)
    outer_xpos = int(xpos + math.sin(angle) * outer)
    outer_ypos = int(ypos - math.cos(angle) * outer)
    inner_xpos = int(xpos + math.sin(angle) * inner)
    inner_ypos = int(ypos - math.cos(angle) * inner)
    cv2.line(img, (inner_xpos, inner_ypos), (outer_xpos, outer_ypos),
             (blue, green, red), strength)

def draw_angle_text(img, xpos, ypos, outer, angle, red, green,
                    blue, strength, size, text):
    fontsize = size/680.0
    font = cv2.FONT_HERSHEY_SIMPLEX
    angle = math.radians(angle)
    outer_xpos = int(xpos + math.sin(angle) * outer)
    outer_ypos = int(ypos - math.cos(angle) * outer)
    cv2.putText(img, text, (outer_xpos, outer_ypos), font, fontsize,
                (blue, green, red), strength, cv2.LINE_AA)

def draw_dart(xpos, ypos, size, img, red, green, blue, strength):
    outer_double = int(size/2)
    tmp = outer_double * 0.04705
    inner_double = int(outer_double - tmp)
    outer_tripple = int(outer_double * 0.62941)
    inner_tripple = int(outer_tripple - tmp)
    inner_bull = int(outer_double * 0.03735)
    outer_bull = int(outer_double * 0.09352)
    #print the double rings
    cv2.circle(img, (xpos, ypos), outer_double, (blue, green, red), strength)
    cv2.circle(img, (xpos, ypos), inner_double, (blue, green, red), strength)
    #print the tripple rings
    cv2.circle(img, (xpos, ypos), outer_tripple, (blue, green, red), strength)
    cv2.circle(img, (xpos, ypos), inner_tripple, (blue, green, red), strength)
    #print the bulls eye
    cv2.circle(img, (xpos, ypos), outer_bull, (blue, green, red), strength)
    cv2.circle(img, (xpos, ypos), inner_bull, (blue, green, red), strength)
    #Numbers around the double Line
    text = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
    outer = outer_double*1.09
    text_xpos = xpos-(size*0.025)
    text_ypos = ypos+(size*0.015)
    #Draw lines and text to the correct angle
    for i in range(0, 20):
        angle = 18 * i
        draw_angle_line(img, xpos, ypos, outer_bull, outer_double,
                        angle+9, red, green, blue, strength)
        draw_angle_text(img, text_xpos, text_ypos, outer, angle,
                        red, green, blue, strength, size, str(text[i]))


# Create a black image
img = np.zeros((600, 600, 3), np.uint8)
img[:] = [255, 255, 255]

draw_dart(300, 300, 500, img, 0, 0, 0, 1)


cv2.imshow('frame', img)
#cv2.imwrite('Dart.jpg', img)
cv2.waitKey(0)