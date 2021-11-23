# 1. Сумма ряда 0-100:
import numpy as np
print(np.sum(np.arange(100)))

# Сумма ряда 0-input():
print('Введите длину ряда:')
a = np.arange(int(input()))
print(np.sum(a))

# 3. Среднее среди 100 случайных чисел:
c = np.random.randint(0, 100, 100)
print(np.mean(c))
