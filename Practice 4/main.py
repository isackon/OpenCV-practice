import numpy as np
import cv2

img = cv2.imread('Almaty.jpg', cv2.IMREAD_COLOR)

# img[55, 55] = [255, 255, 255]

img[100:200, 150:250] = [255, 255, 255]

copy_region = img[337:411, 407:694]
img[300:374, 300:587] = copy_region

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()