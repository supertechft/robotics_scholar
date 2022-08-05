import cv2 
import sys
import numpy as np

camera = cv2.VideoCapture(0)

cv2.namedWindow( "output", cv2.WINDOW_AUTOSIZE );
success, frame = camera.read()
if not success:
    print("Cannot read camera frame")
    sys.exit(1)
cv2.imshow("output", frame)
cv2.waitKey()

cv2.namedWindow( "mask", cv2.WINDOW_AUTOSIZE );

while True:

    success, frame = camera.read()
    if not success: 
        break
    
    print("we got a frame!!")
    cv2.imshow("output", frame)
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    low_red = np.array([131, 155, 84]) 
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)

    cv2.imshow("mask", red_mask)

    key = cv2.waitKey()
    if key==ord('q'): 
        break






