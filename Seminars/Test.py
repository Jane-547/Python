"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число
А в целую степень B с помощью рекурсии.
"""
def degree (a, b, c):
    if b != 0:
        c *= a
        b -= 1
    else:
        return c
    return degree(a, b, c)

num1 = int(input("Введи число А: "))

num2 = int(input("Введи число Б: "))

c = 1

print(degree (num1, num2, c))


def my_power(a, b): # Второй вариант
    if b == 0:
        return 1
    else:
        return a * my_power(a, b - 1)


a = int(input())
b = int(input())
print(my_power(a, b))

"""
Дано натуральное чисел N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
"""

def rotate (n):
    if n == 0:
        return " "
    else:
        a = int(input("Value "))
        return rotate(n-1) + f" {a} "


n = int(input("Enter n: "))

print(rotate(n))

"""
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

*Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)*
"""


def check(n):
    i = 2
    for i in range(2, n):
        if n % i == 0:
            return "NO "

    return "YES "


num = int(input("Input number: "))

print (check(num))

"""
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.


1 5 2 1 5 4
"""

from random import randint

n1_set = list(randint(1, 5) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(n1_set)
def change (list):
    min_num = min(list)
    max_num = max(list)
    for i in range(len(list)):
        if list[i] == max_num:
            list[i] = min_num
    return list

print(change(n1_set))

