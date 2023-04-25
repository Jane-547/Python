# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N)
# для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


def triangle(n):
    if n == 1:
        return 1
    return triangle(n - 1) + n


value = int(input('Введите число n: '))
print(f'Факториал {value} = {factorial(value)}')
print(f'Треугольное число {value} = {triangle(value)}')
