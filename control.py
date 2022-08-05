import function as func
import UI
import time


def phonebook():
    while True:
        time.sleep(3)
        match input('Здравствуйте! Что вы хотите сделать? (введите цифру):\n1 --> Добавить контакт\n2 --> Удалить контакт\n3 --> Отобразить все контакты\n4 --> Найти контакт\n5 --> Выход из программы').lower():
            case '1':
                func.add_person()
            case '2':
                func.del_person()
            case '3':
                UI.display()
            case '4':
                func.find_person()
            case '5':
                print('До свидания!')
                exit()
            case _:
                print('Я так еще не умею(((')