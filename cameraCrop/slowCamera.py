import cv2
from imutils.video import FPS


import imutils

cap = cv2.VideoCapture(0)

fps = FPS().start()
while True:
    flag, frame = cap.read()

    # cv2.imshow('Frame', frame)

    if cv2.waitKey(10) == 27:
        break
    fps.update()
    fps.stop()


    print("FPS: ",fps.fps())

    # cv2.destroyAllWindows()