import cv2
img=cv2.imread("yol.webp",0)
cv2.imshow("Resim",img)
imgResized=cv2.resize(img,(200,200))
cv2.imshow("Yeniden Boyutlandırma",imgResized)
imgCropped=img[:200,:300]
cv2.imshow("Kırpılmış Resim",imgCropped)
if cv2.waitKey(0):
    cv2.destroyAllWindows()