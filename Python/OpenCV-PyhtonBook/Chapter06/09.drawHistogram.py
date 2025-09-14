import numpy as np, cv2

def drawHisto(hist, shape=(200, 256)):
    histImg = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = histImg.shape[1] / hist.shape[0]
    
    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = int(round(gap))
        cv2.rectangle(histImg, (x, 0, w, int(h)), 0, cv2.FILLED)
        
    return cv2.flip(histImg, 0)

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter06/images/pixel.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image], [0], None, [32], [0, 256])
histImg = drawHisto(hist)

cv2.imshow("image", image)
cv2.imshow("histImg", histImg)
cv2.waitKey(0)
