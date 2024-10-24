import numpy as np

def f1(x):
    return 1 / np.sqrt(12 * x + 0.5)
def rectangle_method(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        result += f(a + i * h)
    return result * h

a = 0.6
b = 1.4
n = 10

integral_1 = rectangle_method(f1, a, b, n)
print(f"Result of the first integral (rectangle method): {integral_1}")
