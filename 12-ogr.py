import cv2
import matplotlib.pyplot as plt
import numpy as np
cap=cv2.VideoCapture(0)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

img=cv2.imread("yol.webp",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.show()
edges=cv2.Canny(image=img,threshold1=0,threshold2=255)
plt.figure()
plt.imshow(edges,cmap="gray")
plt.show()
medyan=np.median(img)

low=int(max(0,(1-0.33)*medyan))
high=int(min(0,(1+0.33)*medyan))
#blur
blur=cv2.blur(img,ksize=(7,7))
edges=cv2.Canny(image=blur,threshold1=low,threshold2=high)
plt.figure()
plt.imshow(edges,cmap="gray")
plt.show()


if cv2.waitKey(0):
    cv2.destroyAllWindows()

