import numpy as np


# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("Original Array:")
# print(arr)
# print(arr.shape)
# print(arr[1,2])  # Accessing element at 2nd row, 3rd column

# # Reshaping the array
# zeroes = np.zeros((3, 3))
# print("\nArray of Zeroes:")
# print(zeroes)

# # Creating an array of ones
# ones = np.ones((2, 4))
# print("\nArray of Ones:")
# print(ones)


# range_arr = np.arange(10, 20, 2)
# print("\nArray with Range of Values:")
# print(range_arr)

# linspace_arr = np.linspace(0, 1, 5)
# print("\nArray with Linearly Spaced Values:")
# print(linspace_arr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# reshaped_arr = arr.reshape((2, 4))
# print("\nReshaped Array:")
# print(reshaped_arr)
# flattened_arr = reshaped_arr.flatten()
# print("\nFlattened Array:")
# print(flattened_arr)


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# sum_arr = a + b
# print("\nSum of Arrays:")
# print(sum_arr)
# prod_arr = a * b
# print("\nProduct of Arrays:")
# print(prod_arr) 

# sqrt_arr = np.sqrt(a)
# print("\nSquare Root of Array:")
# print(sqrt_arr)


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Sum of all elements:", np.sum(arr))
print("Mean of all elements:", np.mean(arr))
print("Standard Deviation of all elements:", np.std(arr))
