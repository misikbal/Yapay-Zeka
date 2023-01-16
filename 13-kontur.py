import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("kontur.jpg")
plt.figure(), plt.imshow(img,cmap="gray"),plt.axis("off")
_,contours,hierarch=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
