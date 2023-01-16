import cv2
import numpy as np
from collections import deque
import time
#nesne merkezine depolayacak veri tipi
buffer_size=16
pts=deque(maxlen=buffer_size)

#kırmızı renk aralığı HSV  Ton Doygunluk Parlaklık

redLower=(0,98,0)
redUpper=(28,255,255)


#capture video

cap=cv2.VideoCapture(0)
#video boyut genişlil yükseklik
cap.set(3,1920)
cap.set(4,1080)

while True:
    success,imgOriginal=cap.read()
    if success:
        #blur
        blurred=cv2.GaussianBlur(imgOriginal,(11,11),0)

        #bgr to hsv
        hsv=cv2.cvtColor(imgOriginal,cv2.COLOR_BGR2HSV)

        

        #kırmızı maske
        mask=cv2.inRange(hsv,redLower,redUpper)
        #gürültü silme
        mask=cv2.erode(mask,None,iterations=3)
        mask=cv2.dilate(mask,None,iterations=3)
        

        #konturlama

        (contours,_)=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        center=None
        if len(contours)>0:
            #en büyük konturu al
            c=max(contours,key=cv2.contourArea)

            #dikdörtegene çevir ve çiz
            rect=cv2.minAreaRect(c)

            #x y kordinat, genişlik yükseklik ve açı rotasyon
            ((x,y),(width,height),rotation)=rect
            s=f"x: {np.round(x)}, y:{np.round(y)}, width:{np.round(width)}, height:{np.round(height)}, rotation:{np.round(rotation)}"
            
            print(s)
            # time.sleep(0.1)
            #kutucuk
            box=cv2.boxPoints(rect)
            box=np.int64(box)

            #moment görüntünün merkezini bulmak
            M=cv2.moments(c)
            center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
            #kontur çizdirme
            cv2.drawContours(imgOriginal,[box],0,(0,255,255),2)
            #merkez noktası çizme
            cv2.circle(imgOriginal,center,5,(255,0,255),-1)
            #ekrana yazdırma
            cv2.putText(imgOriginal,s,(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)
        #deque takip
        for i in range(1,len(pts)):
            if pts[i-1] is None or pts[i] is None: continue
            cv2.line(imgOriginal,pts[i-1],pts[i],(0,255,0),3)
        pts.appendleft(center)
        cv2.imshow("Renk Tanimlama",imgOriginal)

    if cv2.waitKey(1) & 0xFF==ord("q"):break