import numpy as np

# Exercise 01: Create a null vector that contains 10 elements
print("Exercise 01: Create a null vector that contains 10 elements")
null_vector = np.zeros(10)
print(null_vector)
print('*****')

# Exercise 02: Create a vector of ones with 10 elements
print("Exercise 02: Create a vector of ones with 10 elements")
vector_ones = np.ones(10)
print(vector_ones)
print('*****')

# Exercise 03: Investigate the linspace function of numpy and create an array with 10 elements
print("Exercise 03: Investigate the linspace function of numpy and create an array with 10 elements")
array_linspace = np.linspace(0, 10, 10)
print(array_linspace)
print('*****')

# Exercise 04.1: Generate a 1d array with random values using random.rand()
print("Exercise 04: Generate a 1d array with random values")
array_random = np.random.rand(10)
print(array_random)
print("Exercise 04: Generate a 2d array with random values")
array_random = np.random.rand(3, 3)
print(array_random)
print('*****')
# Exercise 04.2: Generate a 1d array with random values using random.randint()
print("Exercise 04: Generate a 1d array with random values")
array_random = np.random.randint(10, size=10)
print(array_random)
print("Exercise 04: Generate a 2d array with random values")
array_random = np.random.randint(10, size=(3, 3))
print(array_random)
print('*****')