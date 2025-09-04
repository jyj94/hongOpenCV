import cv2, numpy as np

image= cv2.imread('Data/lenna.bmp')
edge = cv2.Canny(image, 100, 200)
cv2.imshow('edges', edge)
cv2.imshow('image', image)
cv2.waitKey(0)