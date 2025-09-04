import numpy as np, cv2

def main():
    image = cv2.imread('/home/aa/hongOpenCV/Data/hawkes.bmp', cv2.IMREAD_GRAYSCALE)

    dst = cv2.equalizeHist(image)  # 히스토그램 평활화
    cv2.imshow('image', image)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()