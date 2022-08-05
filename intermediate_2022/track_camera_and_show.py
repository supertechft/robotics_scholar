import cv2 
import sys

camera = cv2.VideoCapture(0)

cv2.namedWindow( "output", cv2.WINDOW_AUTOSIZE );
success, frame = camera.read()
if not success:
    print("Cannot read camera frame")
    sys.exit(1)
cv2.imshow("output", frame)
cv2.waitKey()

while True:

    success, frame = camera.read()
    if not success: 
        break
        
    print("we got a frame!!")
    cv2.imshow("output", frame)

    key = cv2.waitKey()
    if key==ord('q'): 
        break






