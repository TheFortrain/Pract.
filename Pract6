import numpy as np
import matplotlib.pyplot as plt

x_values = np.array([-4, -2, 1, 3, -3, -1, 0.5, 2.5])
f_values = np.array([-8, 10, -8, 20, None, None, None, None])  


def lagrange_interpolation(x, x_values, f_values):
    n = len(x_values)
    L = 0.0
    
    for i in range(n):
        if f_values[i] is None:  
            continue
        
        li = 1.0
        for j in range(n):
            if i != j:
                li *= (x - x_values[j]) / (x_values[i] - x_values[j])
        
        L += f_values[i] * li
    
    return L

for i in range(len(f_values)):
    if f_values[i] is None:
        f_values[i] = lagrange_interpolation(x_values[i], x_values, f_values)

x_plot = np.linspace(min(x_values), max(x_values), 500)
y_plot = [lagrange_interpolation(x, x_values, f_values) for x in x_plot]

for i in range(len(x_values)):
    print(f"f({x_values[i]}) = {f_values[i]:.3f}")


plt.plot(x_plot, y_plot, label='Інтерполяційна функція')
plt.scatter(x_values, f_values, color='red', label='Відомі точки')
plt.title('Інтерполяційний багаточлен Лагранжа')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
