import cv2

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("first_argument")
args = parser.parse_args()
args_new = vars(parser.parse_args())

img = cv2.imread(args_new["first_argument"])


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_image", gray)
cv2.imshow("Loaded_image", img)

cv2.waitKey()
cv2.destroyAllWindows()