import numpy as np
import cv2

imgDir = '/home/aa/hongOpenCV/Data/'

image8 = cv2.imread(imgDir + 'butterfly.jpg', cv2.IMREAD_COLOR)
if image8 is None: raise Exception("file read error")

image16 = np.uint16(image8 * (65535 / 255))
image32 = np.float32(image8 * (1 / 255))

print(f'image8 행렬의 일부\n {image8[10:12, 10:13]}')
print(f'image16 행렬의 일부\n {image16[10:12, 10:13]}')
print(f'image32 행렬의 일부\n {image32[10:12, 10:13]}')

cv2.imwrite('test16.tif', image16)
cv2.imwrite('test32.tif', image32)

cv2.imshow('image16', image16)
cv2.imshow('image32', image32)

cv2.waitKey(0)