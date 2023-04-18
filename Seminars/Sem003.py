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

slovar_1 = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": " S005 ", " V ":" S009 ", " VIII ":" S007 ", "IV":"holla", "1234": "S005"}

list_1 = []
for i in slovar_1:
    if slovar_1[i] not in list_1:
        list_1.append(slovar_1[i])
print(list_1)


#задача 21

test_list = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": " S005 ", " V ":" S009 ", " VIII ":" S007 ", "IV":"holla", "1234": "S005"}
#res = list(set(val for dic in test_list for val in dic.values()))
a = set()

for value in test_list.values():
     a.add(value)

print(sorted(a))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

import random

size = int(input('Введите количество элементов списка: '))
spisok = []
for i in range(size):
    spisok.append(random.randint(-5, 5))
print(spisok)

i = 1
count = 0
for i in range(1, len(list_1)):
    if list_1[i] > list_1[i - 1]:
        count += 1
print(count)