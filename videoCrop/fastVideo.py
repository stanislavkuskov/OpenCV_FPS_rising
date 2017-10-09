from imutils.video import VideoStream,FileVideoStream
from imutils.video import FPS
import time
import cv2

# cap = VideoStream(src=0).start()
cap=VideoStream("../videos/jurassic_park_intro.mp4").start()
time.sleep(1.0)
fps = FPS().start()

while True:

    frame = cap.read()
    # frame=cv2.resize(frame,(640,480))

    #
    edges = cv2.Canny(frame, 100, 150)
    cv2.imshow("Frame", edges)

    if cv2.waitKey(10) == 27:
        break
    fps.update()

    fps.stop()
    print("FPS: ",fps.fps())
    # cv2.destroyAllWindows()