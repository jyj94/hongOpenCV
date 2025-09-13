import cv2, numpy as np

v1 = np.array([1,2,3], np.float32)
v2 = np.array([[1],[2],[3]], np.float32)
v3 = np.array([[1,2,3]], np.float32)

print(f'v1\n{v1}')
print(f'v2\n{v2}')
print(f'v3\n{v3}')

v1Exp = cv2.exp(v1)
v2Exp = cv2.exp(v2)
v3Exp = cv2.exp(v3)

print(f'v1Exp\n{v1Exp}')
print(f'v2Exp\n{v2Exp}')
print(f'v3Exp\n{v3Exp}')

v1Log = cv2.log(v1)
v2Log = cv2.log(v2)
v3Log = cv2.log(v3)

print(f'v1Log\n{v1Log}')
print(f'v2Log\n{v2Log}')
print(f'v3Log\n{v3Log}')