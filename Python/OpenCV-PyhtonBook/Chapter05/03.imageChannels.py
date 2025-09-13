import cv2, numpy as numpy

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter05/images/color.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception('file read error!')
if image.shape[2] != 3: raise Exception('image is not 3 channel.')

bgr = cv2.split(image)
print(f'bgr type: {type(bgr)} {type(bgr[0])} {type(bgr[0][0][0])}')
print(f'element count: {len(bgr)}')

cv2.imshow("image", image)
cv2.imshow("blue channel", bgr[0])
cv2.imshow("green channel", bgr[1])
cv2.imshow("red channel", bgr[2])
cv2.waitKey(0)