import cv2

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter06/images/bright.jpg', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.add(image, 200)
dst2 = cv2.subtract(image, 200)

dst3 = image + 100
dst4 = image - 100

cv2.imshow('original image', image)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.waitKey(0)
