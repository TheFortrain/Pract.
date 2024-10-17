import numpy as np
import matplotlib.pyplot as plt


x = np.array([1.425, 1.430, 1.435, 1.440, 1.445, 1.450, 1.455, 1.460, 1.465])
y = np.array([0.8906, 0.8916, 0.8926, 0.8936, 0.8947, 0.8956, 0.8966, 0.8976, 0.8986])


def newton_interpolation(x, y, x0):
    n = len(x)
    f = np.zeros((n, n))
    f[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            f[i, j] = (f[i+1, j-1] - f[i, j-1]) / (x[i+j] - x[i])
    
    result = f[0, 0]
    product = 1.0
    for i in range(1, n):
        product *= (x0 - x[i-1])
        result += f[0, i] * product
    return result


x_values = [1.422, 1.451]


for x_val in x_values:
    y_val = newton_interpolation(x, y, x_val)
    print(f"f({x_val}) = {y_val:.4f}")


x_plot = np.linspace(min(x), max(x), 100)
y_plot = [newton_interpolation(x, y, xi) for xi in x_plot]

plt.plot(x, y, 'o', label='Дані точки')
plt.plot(x_plot, y_plot, label='Інтерполяційна функція Ньютона')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Інтерполяційна функція Ньютона для варіанта 21')
plt.show()
