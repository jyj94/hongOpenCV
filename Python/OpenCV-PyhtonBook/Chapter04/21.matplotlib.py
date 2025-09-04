import cv2
import matplotlib.pyplot as plt

image = cv2.imread("Data/Lena.png", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

rows, cols = image.shape[:2]
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fig = plt.figure(num=1, figsize=(3, 4))
plt.imshow(image), plt.title("gifure1 = original(bgr)")
plt.axis("off"), plt.tight_layout()
