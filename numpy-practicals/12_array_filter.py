import numpy as np


arr = np.array([41, 42, 43, 44])

x = arr[[True, False, True, False]]

print(x)




arr1 = np.array([41, 42, 43, 44, 45, 46])


filter_arr = []


for element in arr1:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr1[filter_arr]

print(filter_arr)

print(newarr)



arr2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

filter_arr1 = []

for element in arr2:
  if element %2 == 0:
    filter_arr1.append(True)
  else:
    filter_arr1.append(False)

newarr1 = arr2[filter_arr1]

print(filter_arr1)

print(newarr1)


#----------------------------------------------------------------------------------------------------------------------


arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)

print(newarr)



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

filter_arr = arr %2 == 0

newarr = arr[filter_arr]

print(filter_arr)

print(newarr)