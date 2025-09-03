import cv2
from Common.utils import print_matInfo

title1, title2 = '16bit unchanged', '32bit unchanged'
imgDir = '/home/aa/hongOpenCV/Data/'

color2unchanged1 = cv2.imread(imgDir + 'read_16.tif', cv2.IMREAD_UNCHANGED)
color2unchanged2 = cv2.imread(imgDir + 'read_32.tif', cv2.IMREAD_UNCHANGED)


if color2unchanged1 is None or color2unchanged2 is None:
    raise Exception("File read error!")

print("행렬 좌표 (10, 10) 화소 값")

print(f'{title1} 원소 자료형 : {type(color2unchanged1[10, 10][0])}')
print(f'{title1} : {color2unchanged1[10, 10]}')
print(f'{title2} 원소 자료형 : {type(color2unchanged2[10, 10][0])}')
print(f'{title2} : {color2unchanged2[10, 10]}')

print_matInfo(title1, color2unchanged1)
print_matInfo(title2, color2unchanged2)
cv2.imshow(title1, color2unchanged1)
cv2.imshow(title2, color2unchanged2)
cv2.waitKey(0)