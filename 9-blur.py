import cv2
import matplotlib.pyplot as plt


img=plt.imread("city.png")
#ortalama bulanıklaştırma
img=cv2.blur(img,ksize=(7,7))
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()


#gaussion blur
img=cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()

#mediyan blur
img=cv2.medianBlur(img,ksize=3)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()
