import numpy as np, cv2

image1 = cv2.imread('Python/OpenCV-PyhtonBook/Chapter05/images/abs_test1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('Python/OpenCV-PyhtonBook/Chapter05/images/abs_test2.jpg', cv2.IMREAD_GRAYSCALE)

if image1 is None or image2 is None: raise Exception('File read error!')

difImage1 = cv2.subtract(image1, image2)
difImage2 = cv2.subtract(np.int16(image1), np.int16(image2))
absDif1 = np.absolute(difImage2).astype('uint8')
absDif2 = cv2.absdiff(image1, image2)

x, y, w, h = 100, 150, 7, 3
print(f'difImage1 = \n{difImage1[y:y+h, x:x+w]}')
print(f'difImage2 = \n{difImage2[y:y+h, x:x+w]}')
print(f'absDif1 = \n{absDif1[y:y+h, x:x+w]}')
print(f'absDif2 = \n{absDif2[y:y+h, x:x+w]}')

titles = ['image1', 'image2', 'difImage1', 'difImage2', 'absDif1', 'absDif2']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)

    