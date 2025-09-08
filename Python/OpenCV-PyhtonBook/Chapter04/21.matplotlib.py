import cv2
import matplotlib.pyplot as plt

image = cv2.imread("/home/aa/hongOpenCV/Data/lenna.bmp", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

rows, cols = image.shape[:2]
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fig = plt.figure(num=1, figsize=(3, 4))
plt.imshow(image), plt.title("gifure1 = original(bgr)")
plt.axis("off"), plt.tight_layout()

fig = plt.figure(figsize=(6,4))
plt.suptitle('figure2- pyplot image display')
plt.subplot(1,2,1), plt.imshow(rgb_image)
plt.axis([0,cols,rows,0]),plt.title('rgb color')
plt.subplot(1,2,2), plt.imshow(gray_image, cmap='gray')
plt.title('gray_img2')
plt.show()