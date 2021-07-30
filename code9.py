# accessing camera and processing images trough "cv" only without using argparse
# argparse and cv2 libraries ain't working properly

import cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() is False:
    print("error opening the camera")
while capture.isOpened():
    ret, frame = capture.read()
    cv2.imshow("farme", frame)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray_frame", gray_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
