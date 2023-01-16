import cv2
from matplotlib import pyplot as plt
import numpy as np
#Fotoğraf Ekleme İşlemi
image=cv2.imread("balik.png",0)
cv2.imshow("ilk resim",image)
k=cv2.waitKey(0) &0xFF
if k==27:
    cv2.destroyAllWindows()

# Yol Gösterme Scale İşlemleri

img = cv2.imread("yol.webp")
print(img.shape)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image)
plt.show()




# print(gray_image.shape)
# (thresh, blackAndWhiteImage) = cv2.threshold(gray_image, 20, 255, cv2.THRESH_BINARY)
# (thresh, blackAndWhiteImage) = cv2.threshold(gray_image, 80, 255, cv2.THRESH_BINARY)
# (thresh, blackAndWhiteImage) = cv2.threshold(gray_image, 160, 255, cv2.THRESH_BINARY)
# (thresh, blackAndWhiteImage) = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
# plt.imshow(blackAndWhiteImage)
# plt.show()

# output2 = cv2.blur(gray_image, (10, 10))
# plt.imshow(output2)
# plt.show()

# output2 = cv2.GaussianBlur(gray_image, (9, 9), 5)
# plt.imshow(output2)
# plt.show()

# (h, w) = img.shape[:2]
# center = (w / 2, h / 2)
# M = cv2.getRotationMatrix2D(center, 13, scale  =1.1)
# rotated = cv2.warpAffine(gray_image, M, (w, h))
# plt.imshow(rotated)
# plt.show()

# img = cv2.imread("yol.webp")
# gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# (thresh, output2) = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
# output2 = cv2.GaussianBlur(output2, (5, 5), 3)
# output2 = cv2.Canny(output2, 180, 255)
# plt.imshow(output2)
# plt.show()