import cv2
import numpy as np

def main():
    orgImg = cv2.imread('/home/aa/hongOpenCV/Data/kids.png', cv2.IMREAD_COLOR)
    img = cv2.split(orgImg)
    print(img[0].shape)
    Green = np.zeros_like(orgImg)  # orgImg와 같은 크기로 생성
    Red = np.zeros_like(orgImg)  # orgImg와 같은 크기로 생성
    Blue = np.zeros_like(orgImg)  # orgImg와 같은 크기로 생성

    # img2의 초록색 채널에 img[1] 복사
    Green[:, :, 1] = img[1]
    Red[:, :, 2] = img[2]
    Blue[:, :, 0] = img[0]



    cv2.imshow("Original", orgImg)
    cv2.imshow("Green", Green)
    cv2.imshow("Blue", Blue)
    cv2.imshow("Red", Red)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()