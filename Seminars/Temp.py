# for i in range(0, 5, 2):
# print(i)
#
# stroka = "qwerty"
# for el in stroka:
# print(el, end = " ")  # end = " " это чтобы выводилось в строку через пробел, а не в столбец
#
#
# i = 0
# while (i < 5):
# n = int(input("Ввод: "))
# if n == 0:
# break
# i+=1
# else:
# print("Конец")
#
#
#
#
# i = 0
# while (i < 5):
# n = int(input("Ввод: "))
# if n == 0:
# break
# i+=1
# else:
# print("Конец")
#
#
#
# slovar = {"1": "one", "2": "one"}
# print(slovar)
# slovar["privet"] = "one"
# print(slovar)
# # for item in slovar:
# #     print(item, slovar[item])
# spisok = []
# for key, value in slovar.items():
#     spisok.append([key, value])
#
# print(spisok)
#
#
#
# spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(spisok[5:2:-1])
#
# spisok2 = spisok[::-1]
# print(spisok2)

import random
n = int(input("Введите кол-во элементов: "))
x = int(input("Введите число:  "))
for i in range(n):
    a = [random.randint(-10,10)]
print(*a ,end="  ")

min = max(a) - x
el = 0
for i in range(len(a)):
    if abs(a[i] - x) < min:
        min = abs(a[i] - x)
        el = a[i]
print(el)