import numpy as np
import time

#testing the speed at which numpy completes tasks compared to normal python lists
size = 1_000_000

list1 = list(range(size))
list2 = list(range(size))

start = time.time()
result = [a + b for a, b in zip(list1, list2)]
print('List array completion time: ', time.time() - start)

arr1 = np.arange(size)
arr2 = np.arange(size)

start = time.time()
result = arr1 + arr2
print('NumPy array addition time: ', time.time() - start)

#we use numpy over python lists because it is vectorized, uses less space and completes tasks faster

#Creating Arrays
#Basic Array Creation

arr3 = np.array([1, 2, 3]) #1D array
arr4 = np.array([[1, 2], [3, 4]]) #2D array

print(arr3, arr3.shape) #.shape will tell you the dimensions in (rows, columns)
print(arr4, arr4.shape)

print('1D array: ', arr3.ndim) #.ndim lets you know the number of dimensions an array has

#Special Arrays
arr5 = np.zeros((2, 3)) #will create an array of zeros(0) that has 2 rows and 3 columns
print('Special array (zeros): ', arr5)

arr6 = np.ones((2, 3))#will create an array of ones(1) that has 2 rows and 3 columns
print('Special Arrays (ones): ', arr6)

arr7 = np.arange(0, 10, 2) #Start at 0, end before 10, step(skip) by 2
print('Special Arrays (arange): ', arr7)

arr8 = np.linspace(0, 1, 5)
print('Special Arrays (linspace): ', arr8) #5 evenly spaced numbers between 0 and 1

arr9 = np.arange(10) #will give us numbers from 0 - 9
print(arr9[2:5]) #slicing from index 2 to 4
arr9[2:5] = 100 #Assigning a value of '100' to values 2, 3, and 4

matrix = np.arange(12).reshape(3, 4)
print(matrix)
