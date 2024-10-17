import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(x):
    return 2 * np.sin(x) + 2 * x


x_values = np.arange(0.1, 1.1, 0.1)
y_values = f(x_values)


def linear_model(x, a, b):
    return a * x + b

linear_params, _ = curve_fit(linear_model, x_values, y_values)


def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

quadratic_params, _ = curve_fit(quadratic_model, x_values, y_values)


plt.figure(figsize=(10, 6))


plt.plot(x_values, y_values, 'o-', label='Точна функція f(x)', color='blue')


linear_approx = linear_model(x_values, *linear_params)

plt.plot(x_values, linear_approx, 'r--', label='Лінійне наближення')
quadratic_approx = quadratic_model(x_values, *quadratic_params)

plt.plot(x_values, quadratic_approx, 'g-.', label='Квадратичне наближення')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Наближення методом найменших квадратів для f(x)')
plt.legend()
plt.grid(True)


plt.show()


print(f"Лінійна модель: y = {linear_params[0]:.4f}x + {linear_params[1]:.4f}")
print(f"Квадратична модель: y = {quadratic_params[0]:.4f}x^2 + {quadratic_params[1]:.4f}x + {quadratic_params[2]:.4f}")
