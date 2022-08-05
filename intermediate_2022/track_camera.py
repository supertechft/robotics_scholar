
import cv2 

camera = cv2.VideoCapture(0)

while camera:

    success, frame = camera.read()

    if not success: 
        break
        
    print("we got a frame!!")





