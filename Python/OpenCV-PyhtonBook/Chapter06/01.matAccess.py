import numpy as np

def matAccess1(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat[i][j]
            mat[i][j] = k * 2
    
mat = np.arange(10).reshape(2, 5)

print(f'원소 처리 전:\n{mat}')
matAccess1(mat)
print(f'원소 처리 후:\n{mat}')
