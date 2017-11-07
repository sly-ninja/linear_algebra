import numpy as np
M, N = 3, 4
matrix = np.arange(M*N).reshape((M,N))

points = np.mgrid[0:N, 0:M].reshape((2, M*N))

a = np.array([[2, 0],[0, 1]])

new_points = np.linalg.inv(a).dot(points).astype(int)

x, y = new_points.reshape((2, M, N), order='F')

print(x + N*y)




# translating
A = np.matrix([[1, 0, -0.75*20], [0, 1, -0.25*20], [0, 0, 1]]) 
P = np.matrix([[0, 0, 20, 20], [0, 20, 20, 0], [1, 1, 1, 1]])   
translated_matrix = A*P 