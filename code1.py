import cv2

img=cv2.imread('testimg.jpg')

dimensions = img.shape
print(dimensions)
no_of_pixels = img.size
print(no_of_pixels)
img_type = img.dtype
print(img_type)

(b, g, r) = img[200, 200]
print((b, g, r))

img[0:100, 0:100] = (0, 0, 255)
img[300, 300] = (255, 0, 0)

cv2.imshow("frame", img)
cv2.waitKey()

# output:
# (600, 600, 3)
# 1080000
# uint8
