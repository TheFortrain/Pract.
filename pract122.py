import numpy as np

def f2(x):
    return np.sin(x**2 - 1) / (2 * np.sqrt(x))

# Метод Сімпсона
def simpson_method(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        k = a + i * h
        if i % 2 == 0:
            result += 2 * f(k)
        else:
            result += 4 * f(k)
    return result * (h / 3)

a = 1.3
b = 2.1
n = 8

integral_2 = simpson_method(f2, a, b, n)
print(f"Result of the second integral (Simpson method): {integral_2}")
