import numpy as np

a = np.arange(1, 13)
print('Original:', a)
reshaped = a.reshape((3, 4))
print('Reshaped (3x4):\n', reshaped)
