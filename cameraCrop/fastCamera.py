from imutils.video import VideoStream
from imutils.video import FPS
import time
import cv2

cap = VideoStream(src=0).start()
time.sleep(1.0)
fps = FPS().start()

while 1:
    frame = cap.read()
    # frame=cv2.resize(frame,(640,480))
    cv2.imshow("Frame", frame)

    if cv2.waitKey(10) == 27:
        break
    fps.update()
    fps.stop()
    print("FPS: ",fps.fps())
    # cv2.destroyAllWindows()