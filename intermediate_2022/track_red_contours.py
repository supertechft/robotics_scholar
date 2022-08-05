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

rows, cols, _ = frame.shape # rows, cols, channels
x_center = int((cols) / 2) # x_center of screen
x_medium = int((cols) / 2) 
y_center = int((rows) / 2) # y_enter of screen
old_y_center = int((rows) / 2)
y_medium = int((rows) / 2) 

while True:

    success, frame = camera.read()
    if not success: 
        break
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    low_red = np.array([131, 155, 84]) 
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)


    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Countours is a list of rank=3 nparrays of varying dimensions
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True) # Sort contours by area, largest to smallest
    # Establish priority for "large" contours which are closest to center
    try:
        maxArea = cv2.contourArea(contours[0]) # Largest area
        print("maxA", maxArea)
    except:# If no area can be found from the "try"
        print("no")
        maxArea = 0 
        found = True

    error = 0.2
    largeContourPairs = []
    for contour in contours: # Compile large contours
        area = cv2.contourArea(contour)
        if area <= maxArea + maxArea and area >= maxArea - maxArea: # If contour is within area boundaries
            (x, y, w, h) = cv2.boundingRect(contour)
            x_medium = int((x + x + w) / 2) # middle line must be int since pixels are ints
            y_medium = int((y + y + h) / 2) 
            dist = np.sqrt(np.power(x_medium-x_center, 2) + np.power(y_medium-old_y_center, 2)) # 2d distance calc for object centroid to center of screen
            largeContourPairs.append((contour, dist)) # append a contour, dist pair
            found = False
    largeContourPairs = sorted(largeContourPairs, key=lambda largeContourPairs : largeContourPairs[1]) # Sort by dist
    # Now create crosshair to home in on object
    for cnt, dist in largeContourPairs: # iterate over contour frames
        (x, y, w, h) = cv2.boundingRect(cnt)
        x_medium = int((x + x + w) / 2) # middle line must be int since pixels are ints
        y_medium = int((y + y + h) / 2) 
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        break # Just interested in first sorted (used to be on biggest, now it's on closest) rectangle/lines
    # Code for crosshair
    print("cross", x_medium, y_medium)
    cv2.line(frame, (x_medium-100,y_medium), (x_medium+100, y_medium), (0, 255, 255), 3)
    cv2.line(frame, (x_medium, y_medium-100), (x_medium, y_medium+100), (0, 255, 255), 3)    
    
    cv2.imshow("output", frame)
    cv2.imshow("mask", red_mask)

    key = cv2.waitKey()
    if key==ord('q'): 
        break






