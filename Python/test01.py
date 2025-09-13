import numpy as np, cv2

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter05/images/bit_test.jpg', cv2.IMREAD_COLOR)
logo = cv2.imread('Python/OpenCV-PyhtonBook/Chapter05/images/logo.jpg', cv2.IMREAD_COLOR)
if image is None or logo is None: raise Exception('image file error.')

masks = cv2.threshold(logo, 200, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)
mask = cv2.bitwise_or(masks[0], masks[1])
mask = cv2.bitwise_or(mask, masks[2])

logoY, logoX = logo.shape[:2]
imageY, imageX = image.shape[:2]
centerX, centerY = (imageX - logoX) // 2, (imageY - logoY) // 2
roi = image[centerY:centerY + logoY, centerX:centerX + logoX]

dst = cv2.copyTo(logo, mask, roi)

roi[:] = dst[:]

cv2.imshow("result", image)
cv2.waitKey(0)

