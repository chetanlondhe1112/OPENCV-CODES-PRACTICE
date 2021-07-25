# accessing & manipulating pixels in opencv with grayscale images

import cv2

# reading grayscale images

gray_img = cv2.imread('umesh.png', cv2.IMREAD_GRAYSCALE)
gray_img = cv2.resize(gray_img, (400,400))

dimensions = gray_img.shape
print(dimensions)
no_of_pixels = gray_img.size
print(no_of_pixels)
img_type = gray_img.dtype
print(img_type)

i = gray_img[200, 300]
print(i)

# modifying value of pixel

gray_img[0:100, 0:100] = 0      # set pixel to black

cv2.imshow("Frame", gray_img)
cv2.waitKey()

# output:
# (600, 600)
# 360000
# uint8
# 107
