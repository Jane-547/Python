# Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

import random

size = int(input('Введите количество элементов массива: '))
spisok = []
for el in range(size):
    spisok.append(random.randint(-10, 10))
print(spisok)

minimal = int(input('Введите значение минимума: '))
maximal = int(input('Введите значение максимума: '))

result = []

for i in range(size):
    if minimal <= spisok[i] <= maximal:
        result.append(i)

print(result)
