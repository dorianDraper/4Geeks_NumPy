# most commonly functions used in data analysis are:
import numpy as np

# create an array for the example
arr = np.array([1, 2, 3, 4, 5])

# Arithmetic operations
print("Arithmetic operations")
print("Sum: ", np.add(arr, 5))
print("Subtract: ", np.subtract(arr, 5))
print("Product: ", np.multiply(arr, 3))

# Logarithmic and Expotential functions
print("Logarithmic and Expotential functions")
print("Natural logarithm: ", np.log(arr))
print("Exponential: ", np.exp(arr))

# Statistical functions
print("Statistical functions")
print("Mean: ", np.mean(arr))
print("Median: ", np.median(arr))
print("Standard deviation: ", np.std(arr))
print("Variance: ", np.var(arr))
print("Maximum value: ", np.max(arr))
print("Maximum value index: ", np.argmax(arr))
print("Minimum value: ", np.min(arr))
print("Minimum value index: ", np.argmin(arr))
print("Sum of all elements: ", np.sum(arr))

# Rounding functions
print("Rounding functions")
arr_decimal = np.array([1.23, 2.47, 3.56, 4.89])
print("Original array: ", arr_decimal)
print("Rounding: ", np.around(arr_decimal))
print("Minor integer (floor): ", np.floor(arr_decimal))
print("Major integer (ceil): ", np.ceil(arr_decimal))

