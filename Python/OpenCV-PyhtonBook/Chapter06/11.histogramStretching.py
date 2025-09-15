import numpy as np, cv2
from histogram import draw_histo

def searchValueIdx(hist, bias=0):
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i)
        if hist[idx] > 0: return idx
    return -1

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter06/images/hist_stretch.jpg', cv2.IMREAD_GRAYSCALE)

bsize, ranges = [64], [0, 256]
hist = cv2.calcHist([image], [0], None, bsize, ranges)

binWidth = ranges[1] / bsize[0]
low = searchValueIdx(hist, 0) * binWidth
high = searchValueIdx(hist, bsize[0] - 1) * binWidth

idx = np.arange(0, 256)
idx = (idx - low) / (high - low) * 255
idx[0:int(low)] = 0
idx[int(high + 1):] = 255

dst = cv2.LUT(image, idx.astype('uint8'))

histDst = cv2.calcHist([dst], [0], None, bsize, ranges)
histImg = draw_histo(hist, (200, 360))
histDstImg = draw_histo(histDst, (200, 360))

print(f'high: {high}')
print(f'low: {low}')
cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.imshow("histImg", histImg)
cv2.imshow("histDstImg", histDstImg)
cv2.waitKey(0)
