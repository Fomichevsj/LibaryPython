import socket
import threading
import sys
import time

print("""В данной программе доступны следующие функции:
        1. print all - Вывести на экран все киниг
        2. add - Добавить книгу
        3. delete - Удалить книгу по ее названию
        4. find - Найти книгу по ее названию
        5. exit - Выход из программы
        6. help - просмотр меню
        7. count - Вывести количество всех книг в базе
        8. save - Сохранить сделанные изменения
        9. print - Вывести на экран информацию о книге""")

host = "localhost"
port = 1080
sock = socket.socket()
sock.connect((host, port))
bollShutDown = False

def Reciver():
    global bollShutDown
    while 1:
        if bollShutDown:
            print("До свидания")
            exit(0)
        data = sock.recv(1024)
        if data:
            print(data.decode())

def Sender():
    global bollShutDown
    while 1:
        print("Введите комманду")
        cmd = input()
        if cmd == "exit" or cmd == "5":
            #sock.send(b"exit")
            #sock.close()
            bollShutDown = True
            print('Выходим')
            exit(0)
        if cmd == "add" or cmd == "2":
            print("Введите необходимые данные для книги", end="\n")
            print("\tВведите название книги: ", end='')
            name = input()
            print("")
            print("\tВведите год издания книги: ", end='')
            try:
                date = int(input())
            except ValueError:
                print("Дата может быть только числом. Попробуйте заново.")
                break
            print("\tВведите автора книги: ", end='')
            author = input()
            print("")
            print()
            print("\tВведите издательский дом: ", end='')
            publis_house = input()
            sock.send(b"add")
            res = name + " " + author + " " + str(date) + " " + publis_house
            time.sleep(2)
            sock.send(bytearray(res, "utf-8"))#Послать сообщение на сервер
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
            print("""В данной программе доступны следующие функции:
        1. print all - Вывести на экран все киниг
        2. add - Добавить книгу
        3. delete - Удалить книгу по ее названию
        4. find - Найти книгу по ее названию
        5. exit - Выход из программы
        6. help - просмотр меню
        7. count - Вывести количество всех книг в базе
        8. save - Сохранить сделанные изменения
        9. print - Вывести на экран информацию о книге""")
        elif cmd == "print all" or cmd == "1":
            sock.send(bytearray(cmd, "utf-8"))
            time.sleep(2)
        elif cmd == "print" or cmd == '9':
            bookToFind = input('Введите имя киниги: ')
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
            print("""В данной программе доступны следующие функции:
                    1. print all - Вывести на экран все киниг
                    2. add - Добавить книгу
                    3. delete - Удалить книгу по ее названию
                    4. find - Найти книгу по ее названию
                    5. exit - Выход из программы
                    6. help - просмотр меню
                    7. count - Вывести количество всех книг в базе
                    8. save - Сохранить сделанные изменения
                    9. print - Вывести на экран информацию о книге""")

t1 = threading.Thread(target=Reciver)
t2 = threading.Thread(target=Sender)

t1.start()
t2.start()
