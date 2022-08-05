# from ntpath import join
# from os import remove
# from posixpath import split


def add_person():
    name = input("Введите ФИО пользователя:")
    phone = input("Введите номер пользователя:")
    descript = input("Введите описание номера:")
    with open('database.txt', 'a') as f:
        f.writelines(name + ' ')
        f.writelines(phone + ' ')
        f.writelines(descript + ' ')
        f.writelines('\n')
    print(f'Контакт успешно добавлен!')

def del_person():
    search_person = input('Введите данные искомого человека: \n')
    with open('database.txt', 'r') as f:
        data = f.readlines()
        for i in range(len(data)):
            if search_person.lower() in data[i].lower():
                print(f'Контакт: {data[i]} успешно удален!')
                data.remove(data[i])
                break
    with open('database.txt', 'w') as f:
        for el in data:
            f.write(el)
            
def find_person():
    search_person = input('Введите данные искомого человека: \n')
    with open('database.txt', 'r') as f:
        data = f.readlines()
        for i in range(len(data)):
            if search_person.lower() in data[i].lower():
                print(f'По введенным Вами данными найден: \n {data[i].title()}')
                break       
        else:
            print(f'По введенным Вами данными человек не найден!')            