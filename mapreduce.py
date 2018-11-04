
import functools as ft

num_list = [2, 5, 7, 9, 4, 6, 8, 1, 10]
num_evens = list(filter(lambda n: n % 2 == 0, num_list))
print(num_evens)

num_half = list(map(lambda n: n * 1 / 2, num_evens))
print(num_half)

num_sum = ft.reduce(lambda a, b: a + b, num_half)
print(num_sum)
