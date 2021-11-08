# coding: utf
# Поиск минимального элемента из списка
A = [3, 4, 2, 1, 0, 8, 9, -1, 100, 0]
Min = A.pop()
while A:
    a = A.pop()
    if a < Min:
        Min = a
print(Min)
