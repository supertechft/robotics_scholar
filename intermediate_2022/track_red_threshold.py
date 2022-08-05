import cv2 
import sys
import numpy as np
from cv2 import createTrackbar

camera = cv2.VideoCapture(0)

cv2.namedWindow( "output", cv2.WINDOW_AUTOSIZE );
success, frame = camera.read()
if not success:
    print("Cannot read camera frame")
    sys.exit(1)
cv2.imshow("output", frame)
cv2.waitKey()

cv2.namedWindow( "mask", cv2.WINDOW_AUTOSIZE );

low_h = 131
high_h = 179

while True:

    success, frame = camera.read()
    if not success: 
        break
    
    print("we got a frame!!")
    cv2.imshow("output", frame)
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    low_red = np.array([low_h, 155, 84]) 
    high_red = np.array([high_h, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red) 
    
    cv2.imshow("mask", red_mask)

    key = cv2.waitKey()
    if key==ord('q'): 
        break
    elif key==ord('h'):
        low_h = low_h - 5 if low_h>0 else 0
    elif key==ord('H'):
        low_h = low_h + 5 if low_h<(high_h-5) else low_h
    elif key==ord('u'):
        high_h = high_h - 5 if high_h>(low_h-5) else 0
    elif key==ord('U'):
        high_h = high_h + 5 if high_h<(255-5) else high_h

    print("S values: %d %d" % ( low_h, high_h ))

        






