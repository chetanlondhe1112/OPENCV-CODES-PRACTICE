# Reading & writing images
# importing packages
import cv2
import argparse


# creating object for command line arguments
parser = argparse.ArgumentParser()

# adding arguments to object
parser.add_argument("path_image_input", help="define path for image to load")

# accessing arguments
args = parser.parse_args()
# Accessing arguments from dictionary by using vars() function

args_new = vars(parser.parse_args())

# reading image
image = cv2.imread(args_new["path_image_input"])
# showing the loading image
cv2.imshow("Loaded image", image)

# processing image (converting from BGR to Grayscale)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# showing the processed image
cv2.imshow("Gray_image", gray_image)

# writing of image
cv2.imwrite(args_new["path_image_output"], gray_image)


cv2.waitKey(0)
cv2.destroyAllWindows()




