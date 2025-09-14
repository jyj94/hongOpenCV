import numpy as np, cv2

m = np.random.randint(0, 100, 15).reshape(3, 5)

mSort1 = cv2.sortIdx(m, cv2.SORT_EVERY_ROW)
mSort2 = cv2.sortIdx(m, cv2.SORT_EVERY_COLUMN)
mSort3 = np.argsort(m, axis=0)

print(f'm\n{m}')
print(f'mSort1\n{mSort1}')
print(f'mSort2\n{mSort2}')
print(f'mSort3\n{mSort3}')