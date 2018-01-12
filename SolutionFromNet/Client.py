import socket
import threading
import sys
import time

import select

stringMenu = """В данной программе доступны следующие функции:
        1. print all - Вывести на экран все киниг
        2. add - Добавить книгу
        3. delete - Удалить книгу по ее названию
        4. find - Найти книгу по ее названию
        5. exit - Выход из программы
        6. help - просмотр меню
        7. count - Вывести количество всех книг в базе
        8. save - Сохранить сделанные изменения
        9. print - Вывести на экран информацию о книге
        10. update - Изменить информацию о книге"""

print(stringMenu)

host = "localhost"
port = 1080
sock = socket.socket()
sock.connect((host, port))
bollShutDown = False
boolNoSuchElement = False

def Reciver():
    global bollShutDown
    global boolNoSuchElement
    while 1:
        data = None
        if bollShutDown:
            print("До свидания")
            exit(0)
        data = sock.recv(1024)
        if data:
            print(data.decode())
            if data.decode() == "no such element":
                boolNoSuchElement = True

def Sender():
    global bollShutDown
    global boolNoSuchElement
    while 1:
        print("Введите комманду")
        cmd = input()
        if cmd == "exit" or cmd == "5":
            sock.send(b"exit")
            #sock.close()
            bollShutDown = True
            print('Выходим')
            break
        if cmd == "update" or cmd == "10":
            print('Введите книгу которую хотите обновить: ')
            bookToUpdate = input()
            if bookToUpdate == '':
                print('Вы не ввели название киниги. Попробуйте заново.')
                print(stringMenu)
                continue
            sock.send(b'find')  # используем команду find тк она по сути выполняет теже функции
            time.sleep(2)
            sock.send(bytearray(bookToUpdate, "utf-8"))
            time.sleep(3)
            if boolNoSuchElement == True:# Не смогли найти книгу. Значит и поле вводить не нужно
                print('Книга не найдена. Попробуйте уточнить поиск.')
                print(stringMenu)
                boolNoSuchElement = False
                continue
            else:
                print('Книга была найдена')
            print('Введите поле, которое хотите обновить.')
            print("""Доступны следующие варианты: 
            name - название книги
            author - автор книги
            year - год издания книги
            publish home - Изадтельскиц дом
            count - Количество экземпляров книги""")
            fieldToUpdate = input()
            if fieldToUpdate == '':
                print('Вы не ввели поле, которое хотите обновить. Попробуйте использовать команду заново.')
                print(stringMenu)
                continue
            if fieldToUpdate not in ["year", "author", "name", "publish home"]:
                print('Нет поля с названием ', fieldToUpdate, '. Попробуйте заново вызвать команду.')
                print(stringMenu)
                continue
            print('Введите новое значение поля.')
            newValue = input()
            sock.send(b'update')
            time.sleep(2)
            sock.send(bytearray(bookToUpdate + "|" + fieldToUpdate + "|"+ newValue, "utf-8"))
            time.sleep(2)
            continue
        if cmd == "add" or cmd == "2":
            print("Введите необходимые данные для книги", end="\n")
            print("\tВведите название книги: ", end='')
            name = input()
            if name == '':
                print('Вы не ввели имя книги. Попробуйте вызвать команду заново.')
                print(stringMenu)
                continue
            print("")
            print("\tВведите год издания книги: ", end='')
            try:
                date = int(input())
            except ValueError:
                print("Дата может быть только числом. Попробуйте заново.")
                continue
            print("\tВведите автора книги: ", end='')
            author = input()
            if author == "":
                print('Вы не ввели автора книги. Попробуйте заново.')
                print(stringMenu)
                continue
            print("")
            print()
            print("\tВведите издательский дом: ", end='')
            publis_house = input()
            if publis_house == '':
                print('Вы не ввели издательский дом. Попробуйте заново.')
                print(stringMenu)
            sock.send(b"add")
            res = name + "|" + author + "|" + str(date) + "|" + publis_house
            time.sleep(2)
            sock.send(bytearray(res, "utf-8"))#Послать сообщение на сервер
            time.sleep(2)
        elif cmd == "delete" or cmd == "3":
            print("Введите имя киниги для удаления")
            bookName = input()
            sock.send(b"delete")
            time.sleep(2)
            sock.send(bytearray(bookName, "utf-8"))
        elif cmd == "find" or cmd == "4":
            print("Введите имя киниги для поиска")
            bookName = input()
            if bookName == "":
                print("вы не ввели имя книги. Попробуйте снова.")
                continue
            sock.send(b"find")
            time.sleep(2)
            sock.send(bytearray(bookName, "utf-8"))
            time.sleep(2)
        elif cmd == "help" or cmd == "6":
            print(stringMenu)
        elif cmd == "print all" or cmd == "1":
            sock.send(bytearray(cmd, "utf-8"))
            time.sleep(2)
        elif cmd == "print" or cmd == '9':
            bookToFind = input('Введите имя книги: ')
            if bookToFind == "":
                print('Вы не ввели имя книгию. Попробуйте снова.')
                continue
            sock.send(b'find')#используем команду find тк она по сути выполняет теже функции
            time.sleep(2)
            sock.send(bytearray(bookToFind, "utf-8"))
            time.sleep(2)
        elif cmd == "count" or cmd == "7":
            sock.send(bytearray(cmd, "utf-8"))
            time.sleep(2)
        elif cmd == "save" or cmd == "8":
            sock.send(bytearray(cmd, "utf-8"))
        else:
            print("Нет такой команды. повотрите заново.")
            print(stringMenu)

t1 = threading.Thread(target=Reciver)
t2 = threading.Thread(target=Sender)

t1.start()
t2.start()
