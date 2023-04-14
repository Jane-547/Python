# import random

# size = int(input('Введите количество элементов списка: '))
# spisok = []
# for i in range(size):
#     spisok.append(random.randint(-5, 5))
# print(spisok)

# viborka = []
# count = 0

# for element in spisok:
#   if element not in viborka:
#     count += 1
#     viborka.append(element)

# print(f'Количество чисел в списке = {len(viborka)}')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# import random
#
# size = int(input('Введите количество элементов списка: '))
# spisok = []
# for i in range(size):
#     spisok.append(random.randint(-5, 5))
# print(spisok)
#
# move = int(input('Введите число k: '))
#
# last_move = spisok[-move:] + spisok[:-move]
# print(last_move)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------------------------------------------------------------------

import random

size = int(input('Введите количество элементов списка: '))
spisok = []
for i in range(size):
    spisok.append(random.randint(-5, 5))
print(spisok)

count = 0
i = 1
for i in spisok:
    if spisok[i] > spisok[i-1]:
        count += 1

print(count)