import cv2, numpy as np

image = cv2.imread('Data/lenna.bmp')
simple_bluerred =cv2.blur(image, (15, 15))
gaussian_blurred = cv2.GaussianBlur(image, (15, 15), 0)
bluerred = cv2.bilateralFilter(image, d=15, sigmaColor=75, sigmaSpace=75)

cv2.imshow('image', image)
cv2.imshow('simple_bluerred', simple_bluerred)
cv2.imshow('gaussian_blurred', gaussian_blurred)
cv2.imshow('bilateralFilter', bluerred)
cv2.waitKey(0)  
