import numpy as np

def f3(x):
    return 1 / np.sqrt(1 + 2 * x**2)

# Метод трапецій
def trapezoidal_method(f, a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

a = 0.6
b = 1.5
n = 20

integral_3 = trapezoidal_method(f3, a, b, n)
print(f"Result of the third integral (trapezoidal method): {integral_3}")
