import pandas as pd
import numpy as np

# Дані на основі зображення
data = {
    'X': [1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2],
    'Y': [0.55, 0.88, 0.94, 1.1, 1.14, 1.14, 0.75, 0.54, 0.55, 0.54, 0.4]
}

# Створення DataFrame
df2 = pd.DataFrame(data)

# Функція для обчислення площі методом трапецій
def Dubno_trapezoid(df2):
    # Крок інтегрування
    h = df2['X'].iloc[1] - df2['X'].iloc[0]
    
    # Початкове значення площі (з першої і останньої точки)
    S = (df2['Y'].iloc[0] + df2['Y'].iloc[-1]) / 2
    
    # Додавання значень всіх середніх точок
    for i in range(1, len(df2)-1):
        S += df2['Y'].iloc[i]
    
    # Повертаємо результат, враховуючи крок h
    return S * h

# Результат власної реалізації
result_custom = Dubno_trapezoid(df2)
print(f'Результат власної реалізації: {result_custom}')

# Перевірка за допомогою вбудованої функції numpy.trapz
result_numpy = np.trapz(df2['Y'], df2['X'])
print(f'Результат за допомогою numpy.trapz: {result_numpy}')
