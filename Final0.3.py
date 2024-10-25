import pandas as pd
import numpy as np

# Дані для X та Y
data = {
    'X': [-4.8, -4.6, -4.4, -4.2, -4.0, -3.8, -3.6, -3.4, -3.2, -3.0, 
          -2.8, -2.6, -2.4, -2.2, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0, 
          -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    'Y': [4.05, 3.6, 3.3, 3.91, 2.6, 2.6, 2.61, 2.3, 2.2, 1.1, 
          0.16, 0.1, 0.3, 0.44, 0.3, 0.7, 1.1, 1.0, 0.87, 0.73, 
          0.83, 0.9, 0.99, 0.6, 0.4, 0.54, 0.55, 0.54, 0.6, 0.65]
}

# Створюємо DataFrame
df1 = pd.DataFrame(data)

# Реалізація методу трапецій вручну
def Dubno_trapezoid(df1):
    h = df1['X'].iloc[1] - df1['X'].iloc[0]  # Крок по осі X
    S = (df1['Y'].iloc[0] + df1['Y'].iloc[-1]) / 2  # Половинна сума першого і останнього значення
    for i in range(1, len(df1) - 1):
        S += df1['Y'].iloc[i]  # Додаємо всі інші значення
    return S * h  # Враховуємо крок інтегрування

# Результат власної реалізації
result_custom = Dubno_trapezoid(df1)
print(f'Результат власної реалізації: {result_custom}')

# Перевірка за допомогою вбудованої функції numpy.trapz
result_numpy = np.trapz(df1['Y'], df1['X'])
print(f'Результат за допомогою numpy.trapz: {result_numpy}')
