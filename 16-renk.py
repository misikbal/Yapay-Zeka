import cv2
import numpy as np
from collections import deque
import time
buffer_line=16
pts=deque(maxlen=buffer_line)

redlower=(0,60,0)
redupper=(20,255,255)


cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while True:
    success,img=cap.read()
    if success:
        blur=cv2.GaussianBlur(img,(11,11),0)
        hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(hsv,redlower,redupper)
        mask=cv2.erode(mask,None,iterations=3)
        mask=cv2.dilate(mask,None,iterations=3)

        (counters,_)=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        center=None
        if len(counters)>0:
            c=max(counters,key=cv2.contourArea)

            rect=cv2.minAreaRect(c)
            ((x,y),(width,height),rotation)=rect
            print(f"x:{np.round(x)}, y:{np.round(y)}, width:{np.round(width)},height:{np.round(height)},rotation:{np.round(rotation)}")
            box=cv2.boxPoints(rect)
            box=np.int64(box)
            M=cv2.moments(c)
            center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
            cv2.drawContours(img,[box],0,(0,255,255),2)
            # cv2.circle(img,)

            


            


        cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF==ord("q"):break
