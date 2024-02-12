from logger import input_data, print_data, copy_data


def interface():
    print('Добрый день! Это бот-помощник. \n'
          'Что вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные \n'
          '3 - Скопировать данные \n')

    command = int(input('Введите команду: '))

    while command < 1 or command > 3:
        command = int(input('Ошибка! Введите команду: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        copy_data()

interface()