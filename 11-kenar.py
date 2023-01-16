import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("sudoku.png",0)
img=np.float32(img)
plt.figure()
plt.imshow(img,cmap="gray")
plt.show()
#harris corner detection
kenar=cv2.cornerHarris(img,blockSize=2,ksize=3,k=0.04)
plt.figure()
plt.imshow(img,cmap="gray")
plt.show()
kenar=cv2.dilate(kenar,None)
img[kenar>0.2*kenar.max()]=1
plt.figure()
plt.imshow(img,cmap="gray")
plt.show()
#shi tomsai detectino

img=cv2.imread("sudoku.png",0)
img=np.float32(img)
corners=cv2.goodFeaturesToTrack(img,100,0.01,10)
corners=np.int64(corners)

for i in corners:
    x,y=i.ravel()
    cv2.circle(img,(x,y),3,(125,125,125),cv2.FILLED)

plt.figure()
plt.imshow(img,cmap="gray")
plt.show()