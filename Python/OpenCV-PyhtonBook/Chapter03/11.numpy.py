import numpy as np

list1, list2 = [1,2,3], [4, 5.0, 6]
a, b = np.array(list1), np.array(list2)

c = a + b
d = a - b
e = a * b
f = a / b
g = a * 2
h = a + 2

print(f'type of a : {type(a)} {type(a[0])}')
print(f'type of b : {type(b)} {type(b[0])}')
print(f'type of c : {type(c)} {type(c[0])}')
print(f'type of g : {type(g)} {type(g[0])}')

print(a, d, e)
print(f, g, h)