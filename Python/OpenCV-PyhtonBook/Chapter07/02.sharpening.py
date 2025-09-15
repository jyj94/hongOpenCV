import cv2, numpy as np

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter07/images/filter_sharpen.jpg', cv2.IMREAD_GRAYSCALE)

data1 = [
    0, -1, 0,
    -1, 5, -1,
    0, -1, 0
]

data2 = [
    -1, -1, -1,
    -1, 9, -1,
    -1, -1, -1
]

def filter(image, mask):
    row, column = image.shape[:2]
    dst = np.zeros((row, column), np.float32)
    xCenter, yCenter = mask.shape[1] // 2, mask.shape[0] // 2
    
    for i in range(yCenter, row - yCenter):
        for j in range(xCenter, column - xCenter):
            y1, y2 = i - yCenter, i + yCenter + 1
            x1, x2 = j - xCenter, j + xCenter + 1
            roi = image[y1:y2, x1:x2].astype('float32')
            temp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(temp)[0]
    return dst.astype('uint8')

mask1 = np.array(data1, np.float32).reshape((3, 3))
mask2 = np.array(data2, np.float32).reshape((3, 3))

sharpen1 = filter(image, mask1)
sharpen2 = filter(image, mask2)

cv2.imshow("image", image)
cv2.imshow("sharpen1", sharpen1)
cv2.imshow("sharpen2", sharpen2)
cv2.waitKey(0)
    