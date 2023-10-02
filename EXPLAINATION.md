# Object Tracking Code

The `main.py` file contains code for tracking an object in a video stream using OpenCV. The code uses a color-based approach to detect the object and track its movement in real-time.

## Importing Libraries

The first step is to import the required libraries. The code imports `time`, `numpy`, and `cv2` libraries. `time` is used to measure the time taken for each loop iteration, `numpy` is used for numerical operations, and `cv2` is used for image processing.

```python
import time
import numpy as np
import cv2 
```

## Initializing the Video Capture

The code initializes the video capture using the `cv2.VideoCapture()` function. It sets the display width and height to 1280x720 pixels using the `cap.set()` function.

```python
cap = cv2.VideoCapture(0)

dispW=1280
dispH=720

cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
```

## Creating Trackbars

The code creates six trackbars using the `cv2.createTrackbar()` function. These trackbars are used to adjust the lower and upper bounds of the HSV color space for object detection.

```python
cv2.namedWindow('myTracker')

cv2.createTrackbar('Hue Low','myTracker',25,179,onTrack1)
cv2.createTrackbar('Hue High','myTracker',85,179,onTrack2)
cv2.createTrackbar('Sat Low','myTracker',50,255,onTrack3)
cv2.createTrackbar('Sat High','myTracker',255,255,onTrack4)
cv2.createTrackbar('Val Low','myTracker',50,255,onTrack5)
cv2.createTrackbar('Val High','myTracker',255,255,onTrack6)
```

## Reading Frames from the Video Stream

The code reads frames from the video stream using the `cap.read()` function. It flips the frame vertically using the `cv2.flip()` function. It then converts the frame from the BGR color space to the HSV color space using the `cv2.cvtColor()` function.

```python
ret, frame = cap.read()
if not ret:
    break
frame=cv2.flip(frame, 1) # Flip the frame vertically
frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
```

## Object Detection

The code detects the object in the frame using the `cv2.inRange()` function. It creates a mask by thresholding the frame based on the lower and upper bounds of the HSV color space. It then applies the mask to the original frame using the `cv2.bitwise_and()` function to obtain the object.

```python
lowerBound=np.array([hueLow,satLow,valLow])
upperBound=np.array([hueHigh,satHigh,valHigh])
myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
myObject=cv2.bitwise_and(frame,frame, mask=myMask)
```

## Object Tracking

The code tracks the object in the frame by finding the contours of the object using the `cv2.findContours()` function. It sorts the contours based on their area and selects the contour with the largest area as the object. It then draws a green rectangle around the object using the `cv2.rectangle()` function and a pink circle at the center of the rectangle using the `cv2.circle()` function. It also displays the coordinates of the center of the rectangle using the `cv2.putText()` function.

```python
contours,junk=cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
if len(contours)>0:
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    contour=contours[0]
    x,y,w,h=cv2.boundingRect(contour)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3) # Draw a green rectangle
    cx = x + w//2
    cy = y + h//2
    cv2.circle(frame, (cx, cy), 5, pinkColor, -1) # Draw a pink circle at the center of the rectangle
    cv2.putText(frame, f"({cx}, {cy})", (10, 100), font, height, pinkColor, weight) # Display the coordinates of the center of the rectangle
```

## Displaying the Results

The code displays the original frame, the mask, and the object using the `cv2.imshow()` function. It also displays the frame rate using the `cv2.putText()` function.

```python
cv2.imshow("Camera", frame)
cv2.imshow('Mask',myMaskSmall)
cv2.imshow('My Object',myObjectSmall)
```

## Exiting the Program

The code exits the program when the 'q' key is pressed using the `cv2.waitKey()` function.

```python
if cv2.waitKey(1)==ord('q'):
    break
```

## Conclusion

In conclusion, the `main.py` file contains code for tracking an object in a video stream using OpenCV. The code uses a color-based approach to detect the object and track its movement in real-time. It also displays the original frame, the mask, and the object, as well as the frame rate.
The code initializes the video capture using the `cv2.VideoCapture()` function. It sets the display width and height to 1280x720 pixels using the `cap.set()` function.