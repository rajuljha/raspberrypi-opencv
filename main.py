####### 3333 ######
import time
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

dispW=1280
dispH=720

cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

fps=0
pos=(30,60)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1.5
weight=3
myColor=(0,0,255)
pinkColor=(255,0,255)

def onTrack1(val):
    global hueLow
    hueLow=val
    print('Hue Low',hueLow)
def onTrack2(val):
    global hueHigh
    hueHigh=val
    print('Hue High',hueHigh)
def onTrack3(val):
    global satLow
    satLow=val
    print('Sat Low',satLow)
def onTrack4(val):
    global satHigh
    satHigh=val
    print('Sat High',satHigh)
def onTrack5(val):
    global valLow
    valLow=val
    print('Val Low',valLow)
def onTrack6(val):
    global valHigh
    valHigh=val
    print('Val High',valHigh)

cv2.namedWindow('myTracker')

cv2.createTrackbar('Hue Low','myTracker',25,179,onTrack1)
cv2.createTrackbar('Hue High','myTracker',85,179,onTrack2)
cv2.createTrackbar('Sat Low','myTracker',50,255,onTrack3)
cv2.createTrackbar('Sat High','myTracker',255,255,onTrack4)
cv2.createTrackbar('Val Low','myTracker',50,255,onTrack5)
cv2.createTrackbar('Val High','myTracker',255,255,onTrack6)

while True:
    tStart=time.time()
    ret, frame = cap.read()
    if not ret:
        break
    frame=cv2.flip(frame, 1) # Flip the frame vertically
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.putText(frame,str(int(fps))+' FPS',pos,font,height,myColor,weight)
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    myMaskSmall=cv2.resize(myMask,(int(dispW/2),int(dispH/2)))
    myObject=cv2.bitwise_and(frame,frame, mask=myMask)
    myObjectSmall=cv2.resize(myObject,(int(dispW/2),int(dispH/2)))

    contours,junk=cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours)>0:
        contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
        #cv2.drawContours(frame,contours,-1,(255,0,0),3)
        contour=contours[0]
        x,y,w,h=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3) # Draw a green rectangle
        cx = x + w//2
        cy = y + h//2
        cv2.circle(frame, (cx, cy), 5, pinkColor, -1) # Draw a pink circle at the center of the rectangle
        cv2.putText(frame, f"({cx}, {cy})", (10, 100), font, height, pinkColor, weight) # Display the coordinates of the center of the rectangle

    cv2.imshow("Camera", frame)
    cv2.imshow('Mask',myMaskSmall)
    cv2.imshow('My Object',myObjectSmall)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps + .1*(1/loopTime)

cap.release()
cv2.destroyAllWindows()