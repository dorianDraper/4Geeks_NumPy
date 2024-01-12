import numpy as np 

# Exercise 01: Create a vector of zeros with 10 elements
print("Exercise 01: Create a vector of zeros with 10 elements")
vector_zeros = np.zeros(10)
print(vector_zeros)
print('*****')
# Exercise 02: Find the memory size of the array that you just created and print it
#   > to get memory size of an element use itemsize 
#   > to get number of elements in array use size
#   >>to get memorize of array multiply num of elements by mem size of elements
print("Exercise 02: Find the memory size of the array that you just created and print it")
print("Memory size: ", vector_zeros.size * vector_zeros.itemsize)
print('*****')
# Exercise 03: Create a vector of zeros with 10 elements and change the fifth element to 1
print("Exercise 03: Create a vector of zeros with 10 elements and change the fifth element to 1")
vector_zeros = np.zeros(10)
print(vector_zeros)
vector_zeros[4] = 1
print(vector_zeros)
print('*****')
# Exercise 04: Create a vector with values ranging from 10 to 49
print("Exercise 04: Create a vector with values ranging from 10 to 49")
vector_10_49 = np.arange(10, 50) # 50 is not included, we use arange instead of range because it is a numpy array
print(vector_10_49)
print('*****')
# Exercise 05: Create vector from 0 to 9 and invert the vector
print("Exercise 05: Create vector from 0 to 9 and invert the vector")
vector_0_9 = np.arange(10)
print(vector_0_9)
vector_0_9 = vector_0_9[::-1]
print(vector_0_9)
print('*****')
# Exercise 06: Create a 3x3 matrix with values ranging from 0 to 8
print("Exercise 06: Create a 3x3 matrix with values ranging from 0 to 8")
matrix_3x3 = np.arange(9).reshape(3, 3)
print(matrix_3x3)
print('*****')
# Exercise 07: Find the indexes of the nonzero elements of the following array [1, 2, 0, 0, 4, 0], The output should be a tuple of arrays with the indices of non zero values
print("Exercise 07: Find the indexes of the nonzero elements of the following array [1, 2, 0, 0, 4, 0], The output should be a tuple of arrays with the indices of non zero values")
array_non_zero = np.array([1, 2, 0, 0, 4, 0])
print(array_non_zero)
print("Index of non zero elements: ", np.nonzero(array_non_zero))
print('*****')
# find the non zero elements of the array using where method
print("find the non zero elements of the array using where method")
print("Index of non zero elements: ", np.where(array_non_zero != 0))
print('*****')
# Exercise 08: Create a 3x3 identity matrix
print("Exercise 08: Create a 3x3 identity matrix")
identity_matrix = np.identity(3)
print(identity_matrix)
print('*****')
# an identity matrix using eye method
print("an identity matrix using eye method")
identity_matrix = np.eye(3)
print(identity_matrix)
print('*****') 
# Exercise 09: create variable named arr which value should be an array with 3 random values
print("Exercise 09: create variable named arr which value should be an array with 3 random values")
arr = np.random.random(3)
print(arr)
print('*****')
# Exercise 10: Create variable named arr which value should be an array with 10 random values and find the maximum value and minimum value
print("Exercise 10: Create variable named arr which value should be an array with 10 random values and find the maximum value and minimum value")
arr = np.random.random(10)
print(arr)
print("Maximum value: ", arr.max())
print("Minimum value: ", arr.min())
print('*****')
# Exercise 11: Create variable named arr which value should be an array with 10 random values and find the mean value
print("Exercise 11: Create variable named arr which value should be an array with 10 random values and find the mean value")
arr = np.random.random(10)
print(arr)
print("Mean value: ", arr.mean())
print('*****')
# Exercise 12: Create matrix with all values equal to 1 and add 0 as the values that are on the center of the matrix
print("Exercise 12: Create matrix with all values equal to 1 and add 0 as the values that are on the center of the matrix")
matrix_ones = np.ones((5, 5))
print(matrix_ones)
print('*****')
matrix_ones[1:-1, 1:-1] = 0 # 1:-1 means from 1 to the last element -1 means the last element is not included 
print(matrix_ones)
print('*****')
# add 0 as the border of the matrix 
print("add 0 as the border of the matrix ")
matrix_ones = np.ones((5, 5))
matrix_ones[0, :] = 0 # 0 means the first element
matrix_ones[-1, :] = 0 # -1 means the last element
matrix_ones[:, 0] = 0 # 0 means the first element
matrix_ones[:, -1] = 0 # -1 means the last element
print(matrix_ones)
print('*****')
# Exercise 13: Create a matrix which values should be all numbers from 0 to 8 and dimension of the matrix should be 3x3
print("Exercise 13: Create a matrix which values should be all numbers from 0 to 8 and dimension of the matrix should be 3x3")
matrix_3x3 = np.arange(9).reshape(3, 3)
print(matrix_3x3)
print('*****')
# same as above but using diag method
print("same as above but using diag method")
matrix_3x3 = np.diag(np.arange(9).reshape(3, 3))
print(matrix_3x3)
print('*****')
# Exercise 14: Create a 8x8 matrix and fill it with a checkerboard pattern
print("Exercise 14: Create a 8x8 matrix and fill it with a checkerboard pattern")
matrix_8x8 = np.zeros((8, 8))
#print(matrix_8x8)
matrix_8x8[1::2, ::2] = 1 # 1::2 means from 1 to the last element with a step of 2 
matrix_8x8[::2, 1::2] = 1 # ::2 means from 0 to the last element with a step of 2
print(matrix_8x8)
print('*****')
