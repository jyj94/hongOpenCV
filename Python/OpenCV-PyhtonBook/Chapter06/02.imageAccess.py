import numpy as np, cv2, time

def pixelAccess1(image):
    image1 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i][j]
            image1[i][j] = 255 - pixel
    return image1

'''
def pixelAccess2(image):
    image2 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image.item(i, j)
            image2.itemset((i, j), 255 - pixel)
    return image2
'''

def pixelAccess3(image):
    lut = [255 - i for i in range(256)]
    lut = np.array(lut, np.uint8)
    image3 = lut[image]
    return image3

def pixelAccess4(image):
    image4 = cv2.subtract(255, image)
    return image4

def pixelAccess5(image):
    image5 = 255 - image
    return image5

image = cv2.imread('Python/OpenCV-PyhtonBook/Chapter06/images/bright.jpg', cv2.IMREAD_GRAYSCALE)

def timeCheck(func, msg):
    startTime = time.perf_counter()
    retImg = func(image)
    elapsed = (time.perf_counter() - startTime) * 1000
    print(f'{msg} 수행시간: {elapsed:.2}ms')
    return retImg

image1 = timeCheck(pixelAccess1, "방법 1 직접 접근 방식")
#image2 = timeCheck(pixelAccess2, "방법 2 item() 함수 방식")
image3 = timeCheck(pixelAccess3, "방법 3 룩업 테이블 방식")
image4 = timeCheck(pixelAccess4, "방법 4 OpenCV 함수 방식")
image5 = timeCheck(pixelAccess5, "방법 5 ndarray 연산 방식")

cv2.imshow("original", image)
cv2.imshow("image1 - directly access to pixcel", image1)
#cv2.imshow("image2 - item()/itemset()", image2)
cv2.imshow("image3 - LUT", image3)
cv2.imshow("image4 - OpenCV", image4)
cv2.imshow("image5 - ndarray 방식", image5)
cv2.waitKey(0)