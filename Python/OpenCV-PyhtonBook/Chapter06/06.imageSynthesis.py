import numpy as np, cv2

image1 = cv2.imread('Python/OpenCV-PyhtonBook/Chapter06/images/add1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('Python/OpenCV-PyhtonBook/Chapter06/images/add2.jpg', cv2.IMREAD_GRAYSCALE)

alpha, beta = 0.6, 0.7
addImg1 = cv2.add(image1, image2)
addImg2 = cv2.add(image1 * alpha, image2 * beta)
addImg2 = np.clip(addImg2, 0, 255).astype("uint8")
addImg3 = cv2.addWeighted(image1, alpha, image2, beta, 0)

cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.imshow('addImg1', addImg1)
cv2.imshow('addImg2', addImg2)
cv2.imshow('addImg3', addImg3)
cv2.waitKey(0)