import cv2
import time
video="people.mp4"
#video içe aktarma capture
cap=cv2.VideoCapture(video)

if cap.isOpened()==False:
    print("Video hatalı")
while True:
    ret, frame=cap.read()

    if ret==True:
        time.sleep(0.01)
        cv2.imshow("Video",frame)
    else: break

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
