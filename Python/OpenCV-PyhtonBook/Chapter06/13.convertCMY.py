import cv2, numpy as np

BGRImg = cv2.imread('Python/OpenCV-PyhtonBook/Chapter06/images/color_model.jpg', cv2.IMREAD_COLOR)

white = np.array([255, 255, 255], np.uint8)
CMYImg = white - BGRImg
yellow, cyan, magenta = cv2.split(CMYImg)

cv2.imshow("BGRImg", BGRImg)
cv2.imshow("CMYImg", CMYImg)
cv2.imshow("yellow", yellow)
cv2.imshow("cyan", cyan)
cv2.imshow("magenta", magenta)
cv2.waitKey(0)