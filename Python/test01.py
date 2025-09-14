import cv2, numpy as np

img = cv2.imread('Python/OpenCV-PyhtonBook/Chapter06/images/equalize.jpg', cv2.IMREAD_GRAYSCALE)

hsize = 256
ranges = [0, 256]

histImgX = 256
histImgY = 200

hist = cv2.calcHist([img], [0], None, [hsize], ranges)
cv2.normalize(hist, hist, 0, 200, cv2.NORM_MINMAX)

histImg = np.full((histImgY, histImgX), 255, np.uint8)

for i in range(hsize):
    cv2.line(histImg, (i, histImgY), (i, histImgY - int(hist[i])), 0)
    
cv2.imshow("", histImg)
cv2.waitKey(0)