import numpy as np
# Operations between arrays
print("Operations between arrays")
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])
print("Array 1: ", array_1)
print("Array 2: ", array_2)
print("Sum: ", array_1 + array_2)
print("Subtraction: ", array_1 - array_2)
print("Multiplication: ", array_1 * array_2)
print("Division: ", array_1 / array_2)
print('*****')
# Exercise 01: Invert the vector of the previous exercise using ::-1 notation (slicing)
print("Exercise 01: Invert the vector of the previous exercise")
array_10 = np.arange(10)
print(array_10)
array_10 = array_10[::-1]
print(array_10)
print('*****')
# Exercise 02: Invert the vector of the previous exercise using the flip method
print("Exercise 02: Invert the vector of the previous exercise using the flip method")
array_10 = np.arange(10)
print(array_10)
array_10 = np.flip(array_10)
print(array_10)
print('*****')
# Exercise 03: Change the size of a random array of dimensions 5x12 into 12x5
print("Exercise 03: Change the size of a random array of dimensions 5x12 into 12x5")
array_random = np.random.randint(10, size=(5, 12))
print(array_random) 
array_random = array_random.reshape(12, 5)
print(array_random)
print('*****')
# Exercise 04: Convert the list [1, 2, 0, 0, 0, 4, 0] into an array and get the index of the non-zero elements
print("Exercise 04: Convert the list [1, 2, 0, 0, 0, 4, 0] into an array and get the index of the non-zero elements")
list_1 = [1, 2, 0, 0, 0, 4, 0]
array_1 = np.array(list_1)  
print(array_1)
print("Index of the non-zero elements: ", np.nonzero(array_1))
# same as above but using the where method
print("Index of the non-zero elements: ", np.where(array_1 != 0))
print('*****')
# Exercise 05: Convert the list [0, 5, -1, 3, 15] into an array, multiply its values by -2 and obtain the even elements of the array
print("Exercise 05: Convert the list [0, 5, -1, 3, 15] into an array, multiply its values by -2 and obtain the even elements of the array")
list_1 = [0, 5, -1, 3, 15]
array_1 = np.array(list_1)
print(array_1)
array_1 = array_1 * -2
print(array_1)
print("Even elements: ", array_1[array_1 % 2 == 0]) # array_1 % 2 == 0 returns a boolean array
print('*****')
# Exercise 06: Create a random vector of 10 elements and order it from smallest to largest
print("Exercise 06: Create a random vector of 10 elements and order it from smallest to largest")
array_random = np.random.randint(10, size=10)
print(array_random)
array_random.sort()
print(array_random)
print('*****')
# Exercise 07: Generate two random vectors of 8 elements and apply the operations of addition, subtraction and multiplication between them
print("Exercise 07: Generate two random vectors of 8 elements and apply the operations of addition, subtraction and multiplication between them")
array_random_1 = np.random.randint(10, size=8)
array_random_2 = np.random.randint(10, size=8)
print("Array 1: ", array_random_1)
print("Array 2: ", array_random_2)
print("Sum: ", array_random_1 + array_random_2)
print("Subtraction: ", array_random_1 - array_random_2)
print("Multiplication: ", array_random_1 * array_random_2)
print('*****')
# Exercise 08: Convert the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] into an array and transform it into a matrix with rows of 3 columns
print("Exercise 08: Convert the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] into an array and transform it into a matrix with rows of 3 columns")
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array_1 = np.array(list_1)
print(array_1)
array_1 = array_1.reshape(3, 3) # 3 rows and 3 columns
print(array_1)
print('*****')