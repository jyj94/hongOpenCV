import cv2, numpy as np

def printRects(rects):
    print("*" * 58)
    print("사각형 원소\t랜덤 사각형 정보\t\t크기")
    print("*" * 58)
    for i, (x, y, w, h, a) in enumerate(rects):
        print(f'rect{i}\t\t({x:03}, {y:03}) from ({w:03}, {h:03})\t{a:05}')
        
rands = np.zeros((5, 5), np.uint16)
starts = cv2.randn(rands[:, :2], 100, 50)
ends = cv2.randn(rands[:, 2:-1], 300, 50)

sizes = cv2.absdiff(starts, ends)
areas = sizes[:, 0] * sizes[:, 1]
rects = rands.copy()
rects[:, 2:-1] = sizes
rects[:,-1] = areas

idx = cv2.sortIdx(areas, cv2.SORT_EVERY_COLUMN).flatten()

printRects(rects)    
printRects(rects[idx.astype('int')])