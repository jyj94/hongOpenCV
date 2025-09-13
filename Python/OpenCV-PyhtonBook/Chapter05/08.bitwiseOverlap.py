import numpy as np, cv2

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter05/images/bit_test.jpg', cv2.IMREAD_COLOR)
logo = cv2.imread('Python/OpenCV-PyhtonBook/Chapter05/images/logo.jpg', cv2.IMREAD_COLOR)
if image is None or logo is None: raise Exception('image file error.')

masks = cv2.threshold(logo, 220.0, 255.0, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fgPassMask = cv2.bitwise_or(masks[0], masks[1])
fgPassMask = cv2.bitwise_or(fgPassMask, masks[2])
bgPassMask = cv2.bitwise_not(fgPassMask)


(H, W), (h, w) = image.shape[:2], logo.shape[:2]
x, y = (W-w) // 2, (H-h) // 2 #길이 만큼 빼서 나누기 2 중앙 값
roi = image[y:y+h, x:x+w] #자를 영역 참조

foreground = cv2.bitwise_and(logo, logo, mask=fgPassMask)
background = cv2.bitwise_and(roi, roi, mask=bgPassMask)

dst = cv2.add(background, foreground)
roi[:] = dst[:]

cv2.imshow('fgPassMask', fgPassMask)
cv2.imshow('bgPassMask', bgPassMask)
cv2.imshow('foreground', foreground)
cv2.imshow('background', background)
cv2.imshow('dst', dst)
cv2.imshow('image', image)

cv2.waitKey(0)

'''
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

'''