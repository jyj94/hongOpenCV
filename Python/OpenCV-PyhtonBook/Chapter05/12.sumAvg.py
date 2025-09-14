import numpy as np, cv2

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter05/images/sum_test.jpg', cv2.IMREAD_COLOR)

mask = np.zeros(image.shape[:2], np.uint8)
mask[60:160, 20:120] = 255

sumValue = cv2.sumElems(image)
meanValue1 = cv2.mean(image)
meanValue2 = cv2.mean(image, mask=mask)

print(f'sumValue 자료형: {type(sumValue), type(sumValue[0])}')
print(f'sumValue: {sumValue}')
print(f'meanValue1: {meanValue1}')
print(f'meanValue2: {meanValue2}')

mean, stddev = cv2.meanStdDev(image)
mean2, stddev2  = cv2.meanStdDev(image, mask=mask)
print(f"mean 자료형 : {type(mean)}, {type(mean[0][0])}")
print(f'mean: {mean.flatten()}')
print(f'mean2: {mean2.flatten()}')
print(f'stddev: {stddev.flatten()}')
print(f'stddev2: {stddev2.flatten()}')

cv2.imshow("image", image)
cv2.imshow("mask", mask)
cv2.waitKey(0)