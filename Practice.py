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



