import cv2
from imutils.video import FPS

cap = cv2.VideoCapture(1)

fps = FPS().start()
while True:
    flag, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    edges = cv2.Canny(frame,100,150)
    cv2.imshow('Frame', edges)

    if cv2.waitKey(10) == 27:
        break
    fps.update()
    fps.stop()


    print("FPS: ",fps.fps())

    # cv2.destroyAllWindows()