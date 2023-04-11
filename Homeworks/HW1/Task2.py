# Задача 2: Найдите сумму цифр трехзначного числа.

number = input('Введите трехзначное число: ')

if int(number) < 100 or int(number) > 999:
    print('Вы ввели не трехзначное число')
else:
    amount = (int(number[0]) + int(number[1]) + int(number[2]))
    print(amount)
