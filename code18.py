import numpy as np
import matplotlib.pyplot as plt
import cv2

image = np.zeros((800, 800, 3), dtype="uint8")

def get_one_contour():
     cnts = [np.array([[[600, 320]], [[563, 460]], [[460, 562]], [[320, 600]], [[180, 563]],[[78, 460]],
            [[40, 320]], [[77, 180]], [[179, 78]], [[319, 40]], [[459,77]], [[562, 179]]], dtype=np.int32)]
     return cnts

contours = get_one_contour()
print("'detected' contours: '{}' ".format(len(contours)))
print("contour shape: '{}'".format(contours[0].shape))
print(contours)

squeeze = np.squeeze(contours)
print(squeeze)

for p in squeeze:
    tuple(p.reshape(1, -1)[0])
    cv2.circle(image, p, 10,  (255, 0, 0), -1)

plt.imshow(image)
plt.title('Title')
plt.show()