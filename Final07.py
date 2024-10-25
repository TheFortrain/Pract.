import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import simpson

# Введення даних
data = {
    'X': [3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0],
    'Y': [0.35, 0.31, 0.23, 0.26, 0.25, 0.33, 0.26, 0.07, 0.0]
}

# Створення DataFrame
df = pd.DataFrame(data)

# Метод середніх прямокутників
x_values = df['X']
y_values = df['Y']

# Обчислення інтегралу методом середніх прямокутників
integral = 0
n = len(x_values) - 1  # кількість інтервалів

for i in range(n):
    # Ширина кожного інтервалу
    h = x_values[i+1] - x_values[i]
    # Середнє значення на інтервалі
    f_avg = (y_values[i] + y_values[i+1]) / 2
    # Площа прямокутника
    integral += h * f_avg

# Виведення результату методу середніх прямокутників
print("Метод середніх прямокутників")
print(f"Інтеграл: {integral:.6f}")

# Перевірка за допомогою вбудованої функції Сімпсона
result_scipy = simpson(y=df['Y'], x=df['X'])

# Виведення результату методу Сімпсона
print("Перевірка методом Сімпсона")
print(f"Інтеграл (метод Сімпсона): {result_scipy:.6f}")

# Побудова графіка для візуалізації
plt.figure(figsize=(8, 4))
plt.plot(df['X'], df['Y'], marker='o', linestyle='-', color='b')

# Налаштування графіка
plt.title('Крива для обчислення площі країни')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

# Показати графік
plt.show()
