import numpy as np, cv2

def makePalette(rows):
    hue = np.arange(0, rows) / rows * 180
    
    hsv = [[(h, 255, 255)] for h in hue]
    hsv = np.array(hsv, np.uint8)
    
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def drawHistHue(hist, shape=(200, 256, 3)):
    hsvPalette = makePalette(hist.shape[0])
    histImg = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    
    gap = histImg.shape[1] / hist.shape[0]
    
    for i, h in enumerate(hist):
        x, w = int(round(i * gap)), int(round(gap))
        color = tuple(map(int, hsvPalette[i][0]))
        cv2.rectangle(histImg, (x, 0, w, int(h)), color, cv2.FILLED)
        
    return cv2.flip(histImg, 0)

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter06/images/hue_hist.jpg', cv2.IMREAD_COLOR)

hsvImg = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hueHist = cv2.calcHist([hsvImg], [0], None, [18], [0, 180])
hueHistImage = drawHistHue(hueHist, (200, 360, 3))

cv2.imshow("image", image)
cv2.imshow("hue hist image", hueHistImage)
cv2.waitKey(0)
