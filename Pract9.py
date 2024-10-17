import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Задаємо символьну змінну та функцію
x = sp.symbols('x')
f = sp.cos(3*x - 1) + x

# Знаходимо перші три похідні
f1 = sp.diff(f, x)
f2 = sp.diff(f1, x)
f3 = sp.diff(f2, x)

# Обчислюємо значення функції та похідних в точці x=0
f_x0 = f.subs(x, 0).evalf()
f1_x0 = f1.subs(x, 0).evalf()
f2_x0 = f2.subs(x, 0).evalf()
f3_x0 = f3.subs(x, 0).evalf()

# Многочлен Тейлора третього порядку
T3 = f_x0 + f1_x0*x + (f2_x0/2)*(x**2) + (f3_x0/6)*(x**3)

# Перетворюємо вирази у функції для побудови графіків
f_lambdified = sp.lambdify(x, f)
T3_lambdified = sp.lambdify(x, T3)

# Генеруємо точки для побудови графіків
x_vals = np.linspace(-2, 2, 400)
f_vals = f_lambdified(x_vals)
T3_vals = T3_lambdified(x_vals)

# Побудова графіків
plt.figure(figsize=(8, 6))
plt.plot(x_vals, f_vals, label="f(x) = cos(3x - 1) + x", color='blue')
plt.plot(x_vals, T3_vals, label="Тейлор (3-й порядок)", linestyle='--', color='red')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції та наближення за многочленом Тейлора")
plt.legend()
plt.grid(True)
plt.show()
