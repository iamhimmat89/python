import numpy as np

# Array
numpy_arr_1 = np.array([1, 2, 3, 4, 5])
numpy_arr_2 = numpy_arr_1 + 5
print(numpy_arr_1)
print(numpy_arr_2)
print(np.sin(numpy_arr_1))
print(np.cos(numpy_arr_1))
print(np.log(numpy_arr_1))
print(np.sqrt(numpy_arr_1))
print(np.sum(numpy_arr_1))
print(np.min(numpy_arr_1))
print(np.max(numpy_arr_1))
print(np.sort(numpy_arr_1))

numpy_arr_3 = np.linspace(0, 15, 16) # 0 to 15 divided into 16 parts. by default 50 parts
print(numpy_arr_3)

numpy_arr_4 = np.arange(1, 10, 2) # start, end and skip
print(numpy_arr_4)

numpy_arr_5 = np.logspace(1, 40, 5) # start from 10^1 to 10^40 and divide into 5 parts
print(numpy_arr_5)
print('%2f' % numpy_arr_5[4])

numpy_arr_6 = np.zeros(5)
print(numpy_arr_6)

numpy_arr_7 = np.ones(5)
print(numpy_arr_7)

# 2-D Array
numpy_array_1 = np.array([
    [1, 2, 3, 6, 2, 9],
    [4, 5, 6, 7, 5, 3]
])
print(numpy_array_1)

numpy_array_flatten = numpy_array_1.flatten()
print(numpy_array_flatten)
print(numpy_array_flatten.ndim)
print(numpy_array_flatten.shape)
print(numpy_array_flatten.size)

numpy_array_2 = numpy_array_flatten.reshape(3, 4)
print(numpy_array_2)
print(numpy_array_2.ndim)
print(numpy_array_2.shape)
print(numpy_array_2.size)

numpy_array_3 = numpy_array_flatten.reshape(2, 2, 3)
print(numpy_array_3)
print(numpy_array_3.ndim)
print(numpy_array_3.shape)
print(numpy_array_3.size)


# Matrix
numpy_matrix_1 = np.matrix('1 2 3; 4 5 6; 7 8 9')
numpy_matrix_2 = np.matrix('1 2 3; 4 5 6; 7 8 9')
print(numpy_matrix_1)
print(numpy_matrix_1)

print(np.diagonal(numpy_matrix_1))
print(numpy_matrix_1.min())

numpy_matrix_addition = numpy_matrix_1 + numpy_matrix_2
print(numpy_matrix_addition)

numpy_matrix_multiplication = numpy_matrix_1 * numpy_matrix_2
print(numpy_matrix_multiplication)
