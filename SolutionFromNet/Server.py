import socket
import threading
import sys

import time

import select

from appJson import run

sock = socket.socket()
try:
    sock.bind(('', 1080))#Подключаемся к сокету, привязываем сокет к этому адресу
except OSError:
    print("Нельзя делать более одного подключения сервера")
    exit(1)
sock.listen(20)
conn = []#переменная, которая будет в себе хранить все соединения
data = ''#сообщение приходящее от клиента
listOfbooks = []
boolWasAddCommand = False
boolWasDeleteCommand = False
bollWasFindCommand = False
boolWasUpdateCommand = False
boolWasHardFind = False
def SenderAndRecier():
    global data
    global conn
    global boolWasAddCommand
    global boolWasDeleteCommand
    global bollWasFindCommand
    global boolWasUpdateCommand
    global boolWasHardFind

    while 1:
        print('in reciever')
        time.sleep(2)
        for i in range(len(conn)):
            print('слушаем клиента ', i)
            try:
                ready = select.select(list(conn), [], [], 4)#функция, которая просматривает поочерёдно всех клиентов
                # и тот клиент, который прислал сообщение записывается в функцию ready
                print('Попытаемся получить сообщение.')
                print(ready[0])#тот клиент, который прислал сообщение
                if ready[0]:
                    data = ready[0][0].recv(1024)#клиент с которым взаимодействует сервер
                    print('Количество подключений: ', len(conn))#берём количество клиентов, которые подключены
                    print('Клиент', i,  'активен. Получили сообщение. -> ', data.decode('utf-8'))# decode - перевод строки байтов в обычную строчку tf8-кодировка
                if data:

                    if boolWasAddCommand:
                        print('Прошлая команда была: добавить книгу')
                        msg = run("add", listOfbooks, data.decode("utf-8"))
                        ready[0][0].send(msg.encode())
                        boolWasAddCommand = False
                    if boolWasUpdateCommand:
                        print('Прошлая команда была: обновить книгу')
                        print('Данные для обновлени киниги: ', data.decode('utf-8'))
                        msg = run("update", listOfbooks, data.decode("utf-8"))
                        ready[0][0].send(msg.encode())
                        boolWasUpdateCommand = False
                    if boolWasDeleteCommand:
                        print('Прошлая команда была: удалить книгу')
                        msg = run("delete", listOfbooks, data.decode("utf-8"))
                        ready[0][0].send(msg.encode())
                        boolWasDeleteCommand = False
                    if bollWasFindCommand:
                        print('Прошлая команда была о поиске киги')
                        msg = run("find", listOfbooks, data.decode("utf-8"))
                        ready[0][0].send(msg.encode())
                        bollWasFindCommand = False
                    if boolWasHardFind:
                        print('Прошлая команда была жесткий поиск')
                        msg = run("hardfind", listOfbooks, data.decode("utf-8"))
                        ready[0][0].send(msg.encode())
                        boolWasHardFind = False
                    if data == "add".encode() or data == "2".encode():
                        print('Мы должны добавить книгу в библиоткеу!')
                        boolWasAddCommand = True
                    if data == "update".encode() or data == "10".encode():
                        print('Мы должны обновить книгу')
                        boolWasUpdateCommand = True
                    if data == "delete".encode() or data == "3".encode():
                        print('Мы должны удалить книгу из библиотеки')
                        boolWasDeleteCommand = True
                    if data == "find".encode() or data == "4".encode():
                        print('Нужно найти книгу')
                        bollWasFindCommand = True
                    if data == "hardfind".encode():
                        print("Нужен жесткий поиск")
                        boolWasHardFind = True
                    if data == "print all".encode() or data == "1".encode():
                        print('Должны напечатать все книги')
                        msg = run(str(data.decode("utf-8")), listOfbooks, "")
                        ready[0][0].send(msg.encode())
                    if data == "count".encode() or data == "7".encode():
                        print("Подсчет числа книг")
                        msg = run(str(data.decode("utf-8")), listOfbooks, "")
                        ready[0][0].send(str(msg).encode())#Возращает число
                    if data == "exit".encode() or data == "5":
                        ready[0][0].send('ok Goodbye'.encode())#активный клиент с которым мы работаем
                        for j in range(len(conn)):
                            print('Сравниваем коннекшин ', j)
                            if conn[j] == ready[0][0]:
                                conn.pop(j)#если клиент завершил свою работу, то убираем из списка соединённых клиентов
                                print('Клиент ', j, ' Разорвал соединение')
                                print('Теперь количество клиентов: ', len(conn))
                                break
                    if data == "save".encode() or data == "8".encode():
                        print("Сохраняем файл")
                        msg = run("save", listOfbooks, "")
                        ready[0][0].send(str(msg).encode())
                    print('Пришло сообщение!')
                    print(data.decode())
                    data = 0#обнуляем переменную, которая хранила сообщение от клиента
                ready = None
            except socket.error as e:#обработка исключенй
                if e.errno == 10053:#номер исключения
                    conn.pop(i)#убираем клиента из списка подключённых клиентов
                    print("Подключено пользователй:", len(conn))
                else:
                    raise# возбуждает указанное исключение

def Accepter():
    while 1:
        time.sleep(2)
        print('in accepter')
        global conn#глобальная переменная используется во всём файле и содержит список всех подключённых клиентов
        conn.append(sock.accept()[0])
        print("Подключено пользователй:", len(conn))


t11 = threading.Thread(target=SenderAndRecier)
t3 = threading.Thread(target=Accepter)

t11.start()
t3.start()