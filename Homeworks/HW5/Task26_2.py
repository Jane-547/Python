# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А
# в целую степень B с помощью рекурсии.

def degree(a, b):
    if b == 0:
        return 1
    else:
        return a * degree(a, b - 1)


num_a = int(input('Введите число a: '))
num_b = int(input('Введите число b: '))

if num_a < 0 or num_b < 0:
    print('Вы ввели отрицательное число!')
else:
    print(f'a в степени b = {degree(num_a, num_b)}')
