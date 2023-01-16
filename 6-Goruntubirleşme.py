import cv2
import numpy as np
img=cv2.imread("yol.webp")
cv2.imshow("Orjinal",img)
#yatay
hor=np.hstack((img,img))
cv2.imshow("Horizontal",hor)
#dikey
ver=np.vstack((img,img))
cv2.imshow("Vertical",ver)
if cv2.waitKey(0):
    cv2.destroyAllWindows()