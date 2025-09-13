import cv2, numpy as np

m1 = np.full((500,500), 10, np.uint8)
m2 = np.full((500,500), 100, np.uint8)

mMask = np.zeros(m1.shape, np.uint8)
mMask[:, 255:] = 1

mAdd1 = cv2.add(m1, m2)
mAdd2 = cv2.add(m1, m2, mask=mMask)

mDiv = cv2.divide(m2, m1)

cv2.imshow('m1', m1)
cv2.imshow('m2', m2)
cv2.imshow('mAdd1', mAdd1)
cv2.imshow('mAdd2', mAdd2)

print(mDiv)

cv2.waitKey(0)