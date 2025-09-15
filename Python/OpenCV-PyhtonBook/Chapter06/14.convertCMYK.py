import numpy as np, cv2

BGRImage = cv2.imread("Python/OpenCV-PyhtonBook/Chapter06/images/color_model.jpg", cv2.IMREAD_COLOR)

white = np.array([255, 255, 255], np.uint8)
CMYImage = white - BGRImage

CMY = cv2.split(CMYImage)

blacK = cv2.min(cv2.min(CMY[0], CMY[1]), CMY[2])
Yellow, Magenta, Cyan = CMY - blacK

cv2.imshow("Yellow", Yellow)
cv2.imshow("Magenta", Magenta)
cv2.imshow("Cyan", Cyan)
cv2.imshow("blacK", blacK)
cv2.waitKey(0)
