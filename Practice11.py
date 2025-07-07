# Array Slicing

import numpy as np
'''
arr = ([1,2,3,4,5,6,7,8])
print(arr[1:5])
print(arr[::2])


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
'''

# Copy Function
'''
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
'''


# View Function 
'''
arr =np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)
'''

'''
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
'''


