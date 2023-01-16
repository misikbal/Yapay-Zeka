import cv2
import matplotlib.pyplot as plt

img=cv2.imread("yol.webp")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()

#eşikleme
_, esik_img=cv2.threshold(img,thresh=60,maxval=255,type=cv2.THRESH_BINARY)
_, ters_img=cv2.threshold(img,thresh=60,maxval=255,type=cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(esik_img,cmap="gray")
plt.show()

plt.figure()
plt.imshow(ters_img,cmap="gray")
plt.show()


#uyarlı eşikleme
thresh_img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
plt.figure()
plt.imshow(thresh_img,cmap="gray")
plt.show()
if cv2.waitKey(0):
    cv2.destroyAllWindows()

