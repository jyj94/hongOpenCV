import numpy as np, cv2

ch0 = np.zeros((2, 4), np.uint8) + 10
ch1 = np.ones((2, 4), np.uint8) * 20
ch2 = np.full((2, 4), 30, np.uint8)

list_bgr = [ch0, ch1, ch2]

merge_bgr = cv2.merge(list_bgr)
split_bgr = cv2.split(merge_bgr)

print(f'split_bgr 형태 : {np.array(split_bgr).shape}')
print(f'merge_bgr 형태 : {merge_bgr.shape}')
print(f'ch0 = \n{ch0}')
print(f'ch1 = \n{ch1}')
print(f'ch2 = \n{ch2}')
print(f'merge_bgr = \n{merge_bgr}')

print(f'split bgr[0] = \n{split_bgr[0]}')
print(f'split bgr[1] = \n{split_bgr[1]}')
print(f'split bgr[2] = \n{split_bgr[2]}')