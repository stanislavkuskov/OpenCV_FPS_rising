import cv2
from imutils.video import FPS

cap = cv2.VideoCapture("../videos/jurassic_park_intro.mp4")

fps = FPS().start()
while True:
    flag, frame = cap.read()


    edges = cv2.Canny(frame, 100, 150)
    cv2.imshow('Frame', edges)

    if cv2.waitKey(10) == 27:
        break
    fps.update()

    fps.stop()
    print("FPS: ",fps.fps())
    # cv2.destroyAllWindows()