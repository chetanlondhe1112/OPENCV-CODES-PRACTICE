import cv2
import imutils
from imutils.video import VideoStream
#import argparse

#parser = argparse.ArgumentParser();

#parser.add_argument("-w", "-webcam", default=0, type=int)
#args = parser.parse_args()
#args = vars(parser.parse_args())
#print("args:{}", format(args))
vs = VideoStream(src=0).start()
while 1:
    ret, capture = vs.read()
    frame = imutils.resize(capture, width=450)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()
vs.stop()
