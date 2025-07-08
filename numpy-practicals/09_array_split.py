# Splitting in Array

import numpy as np

arr = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

new_arr = np.array_split(arr, 5)

print(new_arr)


arr1 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

new_arr1 = np.array_split(arr, 7)

print(new_arr1)


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

#-----------------with 2-D Array----------------------------------------------------------------------------------------


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr[0])
print()
print(newarr[1])
print()
print(newarr[2])


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)

# Along columns

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

# h.split opposite of h.stack

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3, axis=1)

print(newarr)

# v.split opposite of v.stack

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.vsplit(arr, 3, axis=1)

print(newarr)

# d.split opposite of d.stack

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.dsplit(arr, 3, axis=1)

print(newarr)
