import numpy as np, cv2

m = np.random.randint(0, 255, 50000, "uint8").reshape(250, 200)

sort1 = cv2.sort(m, cv2.SORT_EVERY_ROW)
sort2 = cv2.sort(m, cv2.SORT_EVERY_COLUMN)
sort3 = cv2.sort(m, cv2.SORT_EVERY_ROW + cv2.SORT_DESCENDING)
sort4 = np.sort(m, axis = 1)
sort5 = np.sort(m, axis = 0)
sort6 = np.sort(m, axis = 1)[:, ::-1]
sort7 = cv2.sort(m, cv2.SORT_ASCENDING)

cv2.imshow("sort1", sort1)
cv2.imshow("m", m)
cv2.imshow("sort2", sort2)
cv2.imshow("sort3", sort3)
cv2.imshow("sort4", sort4)
cv2.imshow("sort5", sort5)
cv2.imshow("sort6", sort6)
cv2.imshow("sort7", sort7)

cv2.waitKey(0)