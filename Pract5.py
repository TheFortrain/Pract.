import numpy as np

# Задана точність
eps = 0.001

# Ітераційні функції
def g_x(y):
    return 1 - np.cos(y) / 2

def g_y(x):
    return np.sin(x + 1) - 1

# Початкові наближення
x0 = 0.5
y0 = 0.5

# Ітераційний процес
def simple_iteration(x0, y0, eps):
    x_n = x0
    y_n = y0
    x_n1 = g_x(y_n)
    y_n1 = g_y(x_n)
    
    while abs(x_n1 - x_n) > eps or abs(y_n1 - y_n) > eps:
        x_n = x_n1
        y_n = y_n1
        x_n1 = g_x(y_n)
        y_n1 = g_y(x_n)
    
    return x_n1, y_n1

# Виклик функції
x_solution, y_solution = simple_iteration(x0, y0, eps)
print(f'Розв\'язок системи:\n x = {x_solution}, y = {y_solution}')
