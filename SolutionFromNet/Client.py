import socket
import threading
import sys
import time

import select

from pip._vendor.appdirs import unicode#функция используется для декодировки

stringMenu = """В данной программе доступны следующие функции:
        1. print all - Вывести на экран все киниг
        2. add - Добавить книгу
        3. delete - Удалить книгу
        4. find - Найти книгу по ее названию
        5. exit - Выход из программы
        6. help - просмотр меню
        7. count - Вывести количество всех книг в базе
        8. save - Сохранить сделанные изменения
        9. print - Вывести на экран информацию о книге
        10. update - Изменить информацию о книге"""

print(stringMenu)

host = "localhost"
port = 1080#номер порта
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
        data = sock.recv(1024)#получаем сообщение от сервера рамзером не боллее 1024 байт
        if data:
            print(unicode(data, errors = 'ignore'))#игнорируем ошибки при декодировании сообщения, которое приходит
            if unicode(data, errors = 'ignore') == "no such element":
                boolNoSuchElement = True

def Sender():
    global bollShutDown
    global boolNoSuchElement
    while 1:
        print("Введите комманду")
        cmd = input()
        if cmd == "exit" or cmd == "5":
            sock.send(b"exit")#передача сообщения в байтах
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
            bookAuthorForUpdate = input('Автор: ')
            if bookAuthorForUpdate == '':
                print('Вы не ввели автора книги. Попробуйте выполнить команду снова.')
                continue
            bookYearForUpdate = input('Год: ')
            if bookYearForUpdate == '':
                print('Вы не ввели год издания. Попробуйте выполнить команду снова.')
                continue
            bookHomeForUpdate = input('Издательский дом: ')
            if bookHomeForUpdate == '':
                print('Вы не ввели издательский дом. Попробуйте выполнить команду снова.')
                continue
            srvMsg = bookToUpdate + "|" + bookAuthorForUpdate + "|" + bookYearForUpdate + "|" + bookHomeForUpdate
            sock.send(b'hardfind')  # используем команду find тк она по сути выполняет теже функции
            time.sleep(2)#останавливаем поток на 2 секунды
            sock.send(bytearray(srvMsg, "utf-8"))#переводит строчку в массив байтов
            time.sleep(2)
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
            sock.send(bytearray(srvMsg + "|" + fieldToUpdate + "|"+ newValue, "utf-8"))
            time.sleep(2)
            continue
        if cmd == "add" or cmd == "2":
            print("Введите необходимые данные для книги")
            name = input("\tВведите название книги: ")#\t- 1 таб
            if name == '':
                print('Вы не ввели имя книги. Попробуйте вызвать команду заново.')
                print(stringMenu)
                continue
            author = input("\tВведите автора книги: ")
            if author == "":
                print('Вы не ввели автора книги. Попробуйте заново.')
                print(stringMenu)
                continue
            try:
                date = int(input("\tВведите год издания книги: "))
            except ValueError:
                print("Дата может быть только числом. Попробуйте заново.")
                continue
            publis_house = input("\tВведите издательский дом: ")
            if publis_house == '':
                print('Вы не ввели издательский дом. Попробуйте заново.')
                print(stringMenu)
            sock.send(b"add")
            res = name + "|" + author + "|" + str(date) + "|" + publis_house#"|" -нумеровка сообщений для отправки на сервер
            time.sleep(2)
            sock.send(bytearray(res, "utf-8"))#Послать сообщение на сервер
            time.sleep(2)
        elif cmd == "delete" or cmd == "3":
            bookName = input("Введите название киниги для удаления: ")
            if bookName == '':
                print('Вы не ввели название книги. Попробуйте выполнить команду снова.')
                continue
            bookAuthorForDelete = input('Введите автора: ')
            if bookAuthorForDelete == '':
                print('Вы не ввели автора книги. Попробуйте повторить команду снова.')
                continue
            bookYearForDelete = input('Введите год издания книги: ')
            if bookYearForDelete == '':
                print('Вы не ввели год издания книги. Попробуйте снова повторить команду.')
                continue
            bookHomeForDelete = input('Введите издательский дом: ')
            if bookHomeForDelete == '':
                print('Вы не ввели издательский дом. Попробуйте повпторить команду позже.')
                continue
            servMsg = bookName + "|" + bookAuthorForDelete + "|" + bookYearForDelete + "|" + bookHomeForDelete
            sock.send(b"delete")
            time.sleep(2)
            sock.send(bytearray(servMsg, "utf-8"))
            time.sleep(2)
        elif cmd == "find" or cmd == "4":
            print("Введите имя киниги для поиска")
            bookName = input()
            if bookName == "":
                print("вы не ввели имя книги. Попробуйте снова.")
                continue
            bookAuthorForFind = input('Введите автора книги: ')
            if bookAuthorForFind == '':
                print('Вы не ввели автора книги. Это поле являетася обязательным. Попробуйте снова выполнить команду.')
                continue
            bookYearForFind = input('Введтие год издания книги: ')
            if bookYearForFind == '':
                print('Вы не ввели год издания книги. Это поле являетася обязательным. Попробуйте снова выполнить команду.')
                continue
            serverMsg = bookName + "|" + bookAuthorForFind + '|' + bookYearForFind#Параметры которые будем отправлять на сервер
            sock.send(b"find")
            time.sleep(2)
            sock.send(bytearray(serverMsg, "utf-8"))
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
            bookAuthorToPrint = input('Введите автора книги: ')
            if bookAuthorToPrint == '':
                print('Вы не ввели автора книги. Попробуйте выполнить команду снова.')
                continue
            bookYearForPrint = input('Введите год издания книги: ')
            if bookYearForPrint == '':
                print('Вы не ввели год издания книги. Попробуйте выполнить команду снова.')
                continue
            srvMsg = bookToFind + "|" + bookAuthorToPrint + "|" + bookYearForPrint
            sock.send(b'find')#используем команду find тк она по сути выполняет теже функции
            time.sleep(2)
            sock.send(bytearray(srvMsg, "utf-8"))
            time.sleep(2)
        elif cmd == "count" or cmd == "7":
            sock.send(bytearray(cmd, "utf-8"))
            time.sleep(2)
        elif cmd == "save" or cmd == "8":
            sock.send(bytearray(cmd, "utf-8"))
        else:
            print("Нет такой команды. повотрите заново.")
            print(stringMenu)

t1 = threading.Thread(target=Reciver)#начинаем поток, который будет получать сообщения от сервера
t2 = threading.Thread(target=Sender)# /// отправлять

t1.start()#запуск потока
t2.start()
