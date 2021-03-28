import numpy as np
import cv2

img = cv2.imread('c:/Users/AKANKSHA D/Desktop/Programming/ERC/line_detection.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#to detect color
lower_hsv = np.array([0,0,160])
upper_hsv = np.array([179,255,255])

mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('image', img)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()