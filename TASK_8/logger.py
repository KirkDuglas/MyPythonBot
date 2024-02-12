from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Выберите вариант: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

def copy_data():
    var_copy = int(input(f'\nИз какого файла перенести данные? \n'
                    f'1 - Из первого файла во второй\n'
                    f'2 - Из второго файла в первый\n'
                    f'Выберите вариант: '))
    if var_copy == 1:
        with open('data_first_variant.csv','r') as file:
            data = file.read()
        with open('data_second_variant.csv','a') as file: 
            file.write(data)
    else:
        with open('data_second_variant.csv','r') as file:
            data = file.read()
        with open('data_first_variant.csv','a') as file: 
            file.write(data)