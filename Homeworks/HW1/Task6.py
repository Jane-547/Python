# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

number = input('Введите шестизначный номер билета: ')

if int(number) < 99999 or int(number) > 1000000:
    print('Вы ввели не шестизначный номер')

else:
    first_part = sum(map(int, number[:3]))
    second_part = sum(map(int, number[3:]))
    if first_part == second_part:
        print('Yes')
    else:
        print('No')
