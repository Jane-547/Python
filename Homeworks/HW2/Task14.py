# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

value_N = int(input('Введите число N: '))

if value_N < 0:
    print('Вы ввели отрицательное значение. Решений нет!')

k_degree = result = 0

while 2 ** k_degree <= value_N:
    result = 2 ** k_degree
    if result <= value_N:
        print(result, end = " ")
        k_degree += 1
