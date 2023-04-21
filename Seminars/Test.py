25. Напишите программу, которая принимает на вход строку, и отслеживает,
сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

ababac
a_1
b_1
a_2
b_2
a_3
c_1

dict1 = dict()

symbols = input("Введите буквы: ")

for syn in symbols:
    if syn in dict1:
        dict1[syn] +=1
    else:
        dict1[syn] = 0

    if dict1[syn] == 0:
        print(syn)
    else:
        print(f"{syn}_{dict1[syn]}")


2. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

text = input("Введите текст: ").lower()
unique_words = set(text.split())
print("Количество различных слов:", len(unique_words))



3. “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”


number = maxNumber = int(input("Введите цифру: "))

while (number != 0):
    #if (number > maxNumber):
    #    maxNumber = number
    maxNumber = number if number > maxNumber else maxNumber
    number = int(input("Введите цифру: "))

print(f"Максимальный элемент: {maxNumber}")