# accessing camera and processing images trough "cv" only without using argparse
# argparse and cv2 libraries ain't working properly
import cv2
capture = cv2.VideoCapture(0)
frame_index = 0
# print(capture)
if capture.isOpened() is False:
    print("error opening the camera")
while 1:
    ret, frame = capture.read()
    cv2.imshow("frame", frame)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray_frame", gray_frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        frame_name = "captured_frame_{}.png".format(frame_index)
        cv2.imwrite(frame_name, frame)
        frame_index += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
