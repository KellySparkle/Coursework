import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Создание объекта
data = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
print("Объект Series:")
print(data)

# Визуализация данных
plt.figure(figsize=(8, 6))
plt.plot(data, marker='o', linestyle='-', label='Series Data')
plt.title('Визуализация объекта')
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)
plt.show()

# Создание нескольких объектов для сравнения
data1 = pd.Series([1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
data2 = pd.Series([5, 4, 3, 2, 1], index=['A', 'B', 'C', 'D', 'E'])

# Визуализация нескольких серий
plt.figure(figsize=(8, 6))
plt.plot(data1, marker='o', linestyle='-', label='Series 1')
plt.plot(data2, marker='s', linestyle='--', label='Series 2')
plt.title('Сравнение двух объектов')
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)
plt.show()

# Визуализация с помощью гистограмм
np.random.seed(0)
random_data = np.random.randn(100)
series = pd.Series(random_data)

plt.figure(figsize=(8, 6))
series.hist(bins=20, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Гистограмма случайных данных')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
