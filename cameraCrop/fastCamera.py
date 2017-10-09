from imutils.video import VideoStream
from imutils.video import FPS
import time
import cv2

cap = VideoStream(src=1).start()
time.sleep(1.0)
fps = FPS().start()

while 1:
    frame = cap.read()

    edges = cv2.Canny(frame,100,150)
    cv2.imshow('Frame', edges)

    if cv2.waitKey(10) == 27:
        break
    fps.update()
    fps.stop()
    print("FPS: ",fps.fps())
    # cv2.destroyAllWindows()