import numpy as np, cv2

m = np.random.rand(3, 5) * 1000 // 10

reduceSum = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_SUM)
reduceAvg = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_AVG)
reduceMax = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_MAX)
reduceMin = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_MIN)

print(f'm\n{m}')
print(f'reduceSum\n{reduceSum}')
print(f'reduceAvg\n{reduceAvg}')
print(f'reduceMax\n{reduceMax}')
print(f'reduceMin\n{reduceMin}')