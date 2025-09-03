import cv2

def print_matInfo(name, image):
    if image.dtype == 'uint8': mat_type = 'CV_8U'
    elif image.dtype == 'int8': mat_type = 'CV_8S'
    elif image.dtype == 'uint16': mat_type = 'CV_16U'
    elif image.dtype == 'int16': mat_type = 'CV_16S'
    elif image.dtype == 'float32': mat_type = 'CV_32F'
    elif image.dtype == 'float64': mat_type = 'CV_64F'
    nchannel = 3 if image.ndim == 3 else 1
    
    print(f'{name},: {image.dtype}, channel({nchannel}) -> mat_type{mat_type}')
    
imgDir = '/home/aa/hongOpenCV/Data/'
title1, title2 = 'gary2gary', 'gary2color'
gray2gary = cv2.imread(imgDir + 'img1.jpg', cv2.IMREAD_GRAYSCALE)
gray2color = cv2.imread(imgDir + 'img1.jpg', cv2.IMREAD_COLOR)

if gray2gary is None or gray2color is None:
    raise Exception("File read error!")

print("행렬 좌표 (100, 100) 화소 값")
print(f'{title1} : {gray2gary[100, 100]}')
print(f'{title2} : {gray2color[100, 100]}')

print_matInfo(title1, gray2gary)
print_matInfo(title2, gray2color)

cv2.imshow(title1, gray2gary)
cv2.imshow(title2, gray2color)
cv2.waitKey(0)