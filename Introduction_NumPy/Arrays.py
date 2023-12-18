import numpy as np

# Create an array
print("Create an array")
a = np.array([1, 2, 3, 4, 5])
print(a)

# Access the third element of the array
print(a[2])
# Change the value of the second element
a[1] = 7
print(a)
# add 10 to all elements
a = a + 10 # or a += 10
print(a)
# calculate the sum of the elements
sum_all = np.sum(a)
print(sum_all)
# create a 2 dimensional array
print("2 dimensional array")
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array_2d)
# create a 3 dimensional array
print("3 dimensional array")
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(array_3d)
# access the second element of the first array of the 3 dimensional array
print("access the second element of the first array of the 3 dimensional array")
print(array_3d[0, 1])
# create an array of zeros
print("array of zeros")
array_zeros = np.zeros((2, 3))
print(array_zeros)
# create an array of ones
print("array of ones")
array_ones = np.ones((2, 3))
print(array_ones)
