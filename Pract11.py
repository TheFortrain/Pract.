import numpy as np

def newton_interpolation(x, x_values, y_values):
    """
    Функція для знаходження інтерпольованого значення функції за допомогою формул Ньютона.
    """
    n = len(x_values)
    y = y_values[0]
    div_diff = y_values.copy()
    for i in range(1, n):
        for j in range(n - i):
            div_diff[j] = (div_diff[j+1] - div_diff[j]) / (x_values[j+i] - x_values[j])
        y += div_diff[0] * prod(x - x_values[j] for j in range(i))
    return y

def prod(factors):
    """
    Функція для обчислення добутку всіх елементів списку factors.
    """
    result = 1
    for factor in factors:
        result *= factor
    return result

def first_derivative(x, x_values, y_values, eps=0.0001):
    """
    Функція для знаходження першої похідної функції в точці x з точністю eps.
    """
    h = eps
    dy = (newton_interpolation(x + h, x_values, y_values) - newton_interpolation(x - h, x_values, y_values)) / (2 * h)
    return dy

def second_derivative(x, x_values, y_values, eps=0.0001):
    """
    Функція для знаходження другої похідної функції в точці x з точністю eps.
    """
    h = eps
    ddy = (newton_interpolation(x + h, x_values, y_values) - 2 * newton_interpolation(x, x_values, y_values) + 
           newton_interpolation(x - h, x_values, y_values)) / (h**2)
    return ddy

x_values = np.array([2.4, 2.6, 2.8, 3.0, 3.2, 3.4])
y_values = np.array([3.526, 3.782, 3.945, 4.043, 4.104, 4.155])
x = 3.2
dy = first_derivative(x, x_values, y_values)
ddy = second_derivative(x, x_values, y_values)

print(f"Перша похідна f'(3.2) = {dy:.4f}")
print(f"Друга похідна f''(3.2) = {ddy:.4f}")
