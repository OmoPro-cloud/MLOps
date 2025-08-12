#Practice Exercise
#Create a 5x5 matrix with values from 1 to 25, reshape it, then extract:

#the second row 

#the first two columns

#the bottom right 2x2 matrix

import numpy as np

arr1 = np.arange(1, 26).reshape(5, 5)
print(arr1)
print('-' * 30)
print(arr1[1])

print(arr1[0, 0], arr1[1, 0], arr1[2, 0], arr1[3, 0], arr1[4, 0])
print(arr1[0, 1], arr1[1, 1], arr1[2, 1], arr1[3, 1], arr1[4, 1])
