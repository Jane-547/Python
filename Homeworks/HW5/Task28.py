# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def summa(a, b):

    if a == 0:
        return b
    return summa(a-1, b+1)


val_a = int(input('Введите число a: '))
val_b = int(input('Введите число b: '))

if val_a < 0 or val_b < 0:
    print('Вы ввели отрицательное число!')
else:
    print(f'Сумма чисел равна {summa(val_a, val_b)}')