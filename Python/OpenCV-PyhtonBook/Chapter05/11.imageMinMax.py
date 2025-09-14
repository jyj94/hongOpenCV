import cv2, numpy as np

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter05/images/minMax.jpg', cv2.IMREAD_GRAYSCALE)

minVal, maxVal, _, _ = cv2.minMaxLoc(image)

ratio = 255 / (maxVal - minVal)
dst = np.round((image - minVal) * ratio).astype('uint8')

minDst, maxDst, _, _ = cv2.minMaxLoc(dst)

print(f'원본 영상 최대값: {maxVal}, 최소값: {minVal}')
print(f'수정 영상 최대값: {maxDst}, 최소값: {minDst}')

cv2.imshow('original', image)
cv2.imshow('dst', dst)
cv2.waitKey(0)