# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

value = int(input('Введите число n: '))

def fib(n):
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  return fib(n-1) + fib(n-2)

sequence_list = [0]
for i in range(1, value):
  sequence_list.append(fib(i))

print(sequence_list)

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

import random

size = int(input('Сколько всего оценок у Васи: '))
mark_list = []
for i in range(size):
    mark_list.append(random.randint(1, 5))
print(mark_list)

min_mark = max_mark = 1
for i in range(size):
  if mark_list[i] < min_mark:
    min_mark = mark_list[i]
  elif mark_list[i] > max_mark:
    max_mark = mark_list[i]
  i += 1
  
for i in range(size):
  if mark_list[i] == max_mark:
    mark_list[i] = min_mark

print(mark_list)

# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

value = int(input('Введите число: '))

llist = []
i = 1

for i in range(1, abs(value)):
  if value % i == 0:
    llist.append(i)

if (len(llist) < 3):
  print(f'{value} - простое число')
else:
  print(f'{value} - не простое число')

# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

import Methods

how_much = int(input('Введите число: '))

Methods.fill_output(how_much)

