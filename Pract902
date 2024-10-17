import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

# Задана функція
def f(x):
    return np.cos(3 * x - 1) + x

# Генеруємо точки для побудови графіка
x_vals = np.linspace(-2.0, 2.0, num=400)

# Побудова оригінального графіка функції
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f(x_vals), label="f(x) = cos(3x - 1) + x", color='blue')

# Створюємо наближення за многочленом Тейлора для різних степенів
degree = 3  # Степінь многочлена Тейлора
taylor_poly = approximate_taylor_polynomial(f, 0, degree, 1)  # Точка розкладу x=0

# Обчислюємо значення многочлена Тейлора
plt.plot(x_vals, taylor_poly(x_vals), label=f"Тейлор, степень = {degree}", color='red', linestyle='--')

# Додаємо підписи
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.0, shadow=True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції та наближення багаточленом Тейлора")
plt.grid(True)
plt.tight_layout()
plt.show()
