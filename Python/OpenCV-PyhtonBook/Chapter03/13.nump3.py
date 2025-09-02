import numpy as np


np.random.seed(10)
a = np.random.rand(2,3)
b = np.random.randn(3,2)
c = np.random.rand(6)
d = np.random.randint(1, 100, 6)
c = np.reshape(c, (2,3))
d = d.reshape(2, -1)

print(f'shape of a {a.shape} \n {a}')
print(f'shape of b {b.shape} \n {b}')
print(f'shape of c {c.shape} \n {c}')
print(f'shape of d {d.shape} \n {d}')


print('다차원 객체 1차원 변환 방법')
print(f'a = {a.flatten()}')
print(f'b = {np.ravel(b)}')
print(f'c = {np.reshape(c, (-1,))}')
print(f'd = {d.reshape(-1,)}')