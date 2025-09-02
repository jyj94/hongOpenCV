import numpy as np
import cv2

def onChange(value, color):
    global image, title
    addValue = image[0][0]
    # red : 1 green : 2 blue : 3
    if color == 1:
        addValue[2] = value
    elif color == 2:
        addValue[1] = value
    elif color == 3:
        addValue[0] = value
    
    image[:] = addValue
    cv2.imshow(title, image)

title = "test"
image = np.zeros((500, 500, 3), np.uint8)

cv2.imshow(title, image)

cv2.createTrackbar('Red', title, 0, 255, lambda v: onChange(v, 1))
cv2.createTrackbar('Green', title, 0, 255, lambda v: onChange(v, 2))
cv2.createTrackbar('Blue', title, 0, 255, lambda v: onChange(v, 3))

cv2.waitKey(0)
cv2.destroyAllWindows()