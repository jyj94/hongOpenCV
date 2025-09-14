import cv2, numpy as np

data = [
    10, 200, 5, 7, 9,
    15, 35, 60, 80, 170,
    100, 2, 55, 37, 70
]
m1 = np.reshape(data, (3, 5))
m2 = np.full((3, 5), 50)

mMin = cv2.min(m1, 30)
mMax = cv2.max(m1, m2)

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(m1)

print(f'm1 = \n{m1}')
print(f'm2 = \n{m2}')
print(f'mMin = \n{mMin}')
print(f'mMax = \n{mMax}')
print(f'm1 min Location = \n{minVal, minLoc}')
print(f'm1 max Location = \n{maxVal, maxLoc}')
