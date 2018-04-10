from numpy import zeros, newaxis
'''
m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
matrix = []; columns = []
# initialize the number of rows
for i in range(0,m):
  matrix += [0]
# initialize the number of columns
for j in range (0,n):
  columns += [0]
# initialize the matrix
matrix = [[0 for j in range(n)] for i in range(m)]
for i in range (0,m):
  for j in range (0,n):
    print ('entry in row: ',i+1,' column: ',j+1)
    matrix[i][j] = int(input())
print (matrix)
matrix_new = matrix[:, :, newaxis]

print(matrix_new.shape)
'''
import numpy as np

# the 2d array of our samples,
# each component is a category label
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
# the 3d array that will be the one-hot representation
# a.max() + 1 is the number of labels we have
b = np.zeros((a.shape[0], a.shape[1], a.max() + 1))

# if you visualize this as a stack of layers,
# where each layer is a sample,
# this first index selects each layer separately
layer_idx = np.arange(a.shape[0]).reshape(a.shape[0], 1)

# this index selects each component separately
component_idx = np.tile(np.arange(a.shape[1]), (a.shape[0], 1))

# then we use `a` to select indices according to category label
b[layer_idx, component_idx, a] = 1

# voila!
print(b)