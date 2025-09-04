import cv2, numpy as np

def main():
    image = cv2.imread('Data/candies.png')
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)


    cv2.imshow('mask1', mask1)
    cv2.imshow('mask2', mask2)
    cv2.imshow('mask', mask)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()