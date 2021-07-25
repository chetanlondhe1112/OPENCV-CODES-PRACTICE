import cv2
import matplotlib as plt

# reading image
img=cv2.imread('umesh.png')
img=cv2.resize(img, (400, 350))
# getting dimension of image using shape
dimensions = img.shape
print(dimensions)

no_of_pixels = img.size
print(no_of_pixels)

img_type = img.dtype
print(img_type)

# accessing pixel value in 3 channels
(b, g, r) = img[200, 200]
print((b, g, r))

# modifying value of pixels
img[0:100, 0:100] = (0, 0, 255)

# modifying value of pixel
img[200, 200] = (255, 0, 0)

# splitting coloured image in 3 channels

b, g, r = cv2.split(img)
cv2.imshow("Blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)


# merging three channels into RGB format

img_matplotlib = cv2.merge([r, g, b])

cv2.imshow("BGR", img)
cv2.imshow("RGB", img_matplotlib)

cv2.imshow("frame", img)
cv2.waitKey()


# (350, 400, 3)
# 420000
# uint8
# (185, 204, 245)