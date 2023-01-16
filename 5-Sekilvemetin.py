import cv2
import numpy as np


img=np.zeros((512,512,3),np.uint8)
#resim,başlangıç noktası,bitiş noktası, renk, kalınlık
#çizgi
cv2.line(img,(100,100),(100,300),(0,0,255),3)
cv2.imshow("Çizgi",img)


#dikdörtgen
cv2.rectangle(img,(0,0),(256,256,),(255,0,0))
cv2.imshow("Diktörgen",img)


#çember
#resim,merkez,yarı çap, renk
cv2.circle(img,(300,300),45,(0,255,0),cv2.FILLED)
cv2.imshow("Çember",img)

#metin
#(resim,başlangıç noktası,font,kalınlığı,renk)
# cv2.daire(img,"Yazi",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))

cv2.imshow("Metin",img)

if cv2.waitKey(0):
    cv2.destroyAllWindows()