import cv2
from imutils.video import FPS

cap = cv2.VideoCapture("../videos/jurassic_park_intro.mp4")

fps = FPS().start()
while True:
    flag, frame = cap.read()
    if not flag:
        break
    # cv2.imshow('Frame', frame)
    cv2.waitKey(1)
    fps.update()
    fps.stop()


    print("FPS: ",fps.fps())

    if cv2.waitKey(10) == 27:
        break

    # cv2.destroyAllWindows()