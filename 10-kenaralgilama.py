import cv2
import matplotlib.pyplot as plt
import numpy as np
# cap=cv2.VideoCapture(0)
# width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# writer=cv2.VideoWriter("kenar.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))

cap=cv2.VideoCapture(0)
#video boyut genişlil yükseklik
cap.set(3,1920)
cap.set(4,1080)

while True:
    success,imgOriginal=cap.read()
    if success:
        # blurred=cv2.GaussianBlur(imgOriginal,(11,11),0)
        edges=cv2.Canny(image=imgOriginal,threshold1=0,threshold2=255)
        cv2.imread("deneme",edges)

    if cv2.waitKey(1)==ord("q"):break

# cap.release()
# writer.release()
# cv2.destroyAllWindows()
# img=cv2.imread("yol.webp",0)
# plt.figure()
# plt.imshow(img,cmap="gray")
# plt.show()
# edges=cv2.Canny(image=img,threshold1=0,threshold2=255)
# plt.figure()
# plt.imshow(edges,cmap="gray")
# plt.show()



# plt.figure()
# plt.imshow(edges,cmap="gray")
# plt.show()


# if cv2.waitKey(0):
#     cv2.destroyAllWindows()

