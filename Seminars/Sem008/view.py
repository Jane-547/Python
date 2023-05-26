from colorama import Fore, Style


def interface():
    print(Fore.YELLOW + "ТЕЛЕФОННАЯ КНИГА" + Style.RESET_ALL)
    print("1. " + Fore.GREEN + "Добавить новый контакт" + Style.RESET_ALL)
    print("2. " + Fore.GREEN + "Показать все контакты" + Style.RESET_ALL)
    print("3. " + Fore.GREEN + "Найти контакт" + Style.RESET_ALL)
    print("4. " + Fore.GREEN + "Изменить контакт" + Style.RESET_ALL)
    print("5. " + Fore.GREEN + "Удалить контакт" + Style.RESET_ALL)
    print("6. " + Fore.RED + "Выход" + Style.RESET_ALL)
    print()
    choice = int(input("Введите цифру для дальнейших действий: "))
    return choice


def ok():
    print(Fore.BLUE + "Данные успешно добавлены!:)" + Style.RESET_ALL + '\n')


def error():
    print(Fore.RED + "Нужно ввести число от 1-6" + Style.RESET_ALL)


def welcome():
    print(Fore.BLUE + 'ПРИВЕТСТВУЮ ВАС!' + '\n' + '----------------------------------------' + '\n' + 'Выберите одно из желаемых вариантов действий:'+ Style.RESET_ALL+'\n')


def goodbye():
    print('Ждем вас снова!')
