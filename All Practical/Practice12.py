# Array Shape


import numpy as np
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr.shape)


arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr1.shape)
'''

# Array Reshape
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
'''


# Flattening the array
'''
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(6)
print(newarr)
'''