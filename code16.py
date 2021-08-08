# construction of basic shapes

import cv2
import matplotlib.pyplot as plt
import numpy as np
# Dictionary containing some colors:
# colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
#          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
 #         'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
  #        'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

image = np.zeros((400, 400, 3), dtype="uint8")
image[:] = (220, 220, 220)
cv2.line(image, (0, 0), (400, 400), (0, 0, 255),3)
cv2.rectangle(image, (100, 100), (200, 200), (0, 0, 255), 3)
cv2.rectangle(image, (300, 300), (200, 200), (0, 0, 255), -1)
cv2.circle(image, (250, 200), (20), 1)
cv2.arrowedLine(image, (230, 340), (370, 360), (0, 255, 0), 3, tipLength=0.2)
cv2.ellipse(image, (167, 279), (40, 60), 0, 0, 360, (255, 0, 0), -1)

plt.imshow(image)
plt.title('title')
plt.show()

image[:] = (255, 255, 255)
cv2.putText(image,'Hey im chetan', (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2, cv2.LINE_AA)
plt.imshow(image)
plt.title('Text')
plt.show()

