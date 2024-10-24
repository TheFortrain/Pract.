import numpy as np
import matplotlib.pyplot as plt


def f_a(x, y):
    return x + np.sin(y / 1.25)


def f_b(x, y):
    return x + np.cos(y / np.sqrt(1.3))


h = 0.1  # Крок
x_a = np.arange(0.5, 1.5 + h, h)  
y0_a = 1.8  


x_b = np.arange(1.2, 2.2 + h, h)  
y0_b = 1.8  

def euler_method(f, x_range, y0):
    y_values = [y0]
    for i in range(1, len(x_range)):
        y_next = y_values[-1] + h * f(x_range[i - 1], y_values[-1])
        y_values.append(y_next)
    return y_values

def euler_cauchy_method(f, x_range, y0):
    y_values = [y0]
    for i in range(1, len(x_range)):
        y_star = y_values[-1] + h * f(x_range[i - 1], y_values[-1])
        y_next = y_values[-1] + h / 2 * (f(x_range[i - 1], y_values[-1]) + f(x_range[i], y_star))
        y_values.append(y_next)
    return y_values

y_euler_a = euler_method(f_a, x_a, y0_a)
y_euler_cauchy_a = euler_cauchy_method(f_a, x_a, y0_a)

y_euler_b = euler_method(f_b, x_b, y0_b)
y_euler_cauchy_b = euler_cauchy_method(f_b, x_b, y0_b)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x_a, y_euler_a, 'b-', label="Euler's Method")
plt.plot(x_a, y_euler_cauchy_a, 'r--', label="Euler-Cauchy's Method")
plt.title("Рівняння (a): Метод Ейлера і Ейлера-Коші")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_b, y_euler_b, 'b-', label="Euler's Method")
plt.plot(x_b, y_euler_cauchy_b, 'r--', label="Euler-Cauchy's Method")
plt.title("Рівняння (b): Метод Ейлера і Ейлера-Коші")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.tight_layout()
plt.show()
