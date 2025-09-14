import numpy as np, cv2

def calcHisto(image, hsize, ranges=[0, 256]):
    hist = np.zeros((hsize, 1), np.float32)
    gap = ranges[1]/hsize
    
    for i in (image/gap).flat:
        hist[int(i)] += 1

    return hist

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter06/images/pixel.jpg', cv2.IMREAD_GRAYSCALE)

hsize, ranges = [32], [0, 256]
gap = ranges[1]/hsize[0]
rangesGap = np.arange(0, ranges[1] + 1, gap)
hist1 = calcHisto(image, hsize[0], ranges)
hist2 = cv2.calcHist([image], [0], None, hsize, ranges)  # OpenCV 함수
hist3, bin = np.histogram(image, rangesGap)

print("User 함수: \n", hist1.flatten())                  # 행렬을 벡터로 변환하여 출력
print("OpenCV 함수: \n", hist2.flatten())                # 행렬을 벡터로 변환하여 출력
print("numpy 함수: \n", hist3.astype(float))             # 행렬을 벡터로 변환하여 출력

cv2.imshow("image", image)
cv2.waitKey(0)