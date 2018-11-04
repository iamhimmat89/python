
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)


def _without_recursion_factorial(n):
    value_factorial = 1
    for i in range(1, n + 1):
        value_factorial = value_factorial * i
    return value_factorial


result_1 = _without_recursion_factorial(5)
print(result_1)


def _with_recursion_factorial(n):
    if n == 0:
        return 1

    return n * _with_recursion_factorial(n-1)


result_2 = _with_recursion_factorial(5)
print(result_2)
