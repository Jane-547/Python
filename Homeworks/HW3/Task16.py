import random

quantity = int(input('Введите количество элементов массива: '))

array = [random.randint(0, 9) for i in range(quantity)]
print(array, end = " ")

element = int(input(f'\nВведите число X: '))

print(f'Количество {element} в массиве - {array.count(element)}')