#import numpy as np
import cv2

cap = cv2.VideoCapture(1)
    
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
#    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
#    hsl = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS_FULL)
#    bit = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # Display the resulting frame
#    cv2.imshow('hsv',hsv)
#    cv2.imshow('hsl',hsl)
#    cv2.imshow('inverse',bit)
    cv2.imshow('normal',frame)
    cv2.imwrite('ring.jpg',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()