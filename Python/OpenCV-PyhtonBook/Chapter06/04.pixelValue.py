import cv2

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter06/images/pixel.jpg', cv2.IMREAD_GRAYSCALE)

(x, y), (w, h) = (180, 37), (15, 10)
roiImg = image[y:y+h, x:x+w]

print('roi =')
for row in roiImg:
    for p in row:
        print(f'{p:4}', end="")
    print()
    
cv2.rectangle(image, (x, y, w, h), 255, 1)
cv2.imshow('image', image)
cv2.waitKey(0)
      