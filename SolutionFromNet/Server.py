import socket
import threading
import sys

import time

import select

from appJson import run

sock = socket.socket()
#sock.bind(('', 1080))
try:
    sock.bind(('', 8080))
except OSError:
    print("Нельзя делать более одного подключения сервера")
    exit(1)
sock.listen(20)
conn = []
data = ''
listOfbooks = []
boolWasAddCommand = False
boolWasDeleteCommand = False
bollWasFindCommand = False
boolWasUpdateCommand = False
def SenderAndRecier():
    global data
    global conn
    global boolWasAddCommand
    global boolWasDeleteCommand
    global bollWasFindCommand
    global boolWasUpdateCommand

    while 1:
        print('in reciever')
        time.sleep(2)
        for i in range(len(conn)):
            print('слушаем клиента ', i)
            try:
                ready = select.select(list(conn), [], [], 4)
                print('Попытаемся получить сообщение.')
                print(ready[0])
                #print(conn[i])
                if ready[0]:
                    data = ready[0][0].recv(1024)
                    print('Количество подключений: ', len(conn))
                    print('Клиент', i,  'активен. Получили сообщение. -> ', data.decode('utf-8'))
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
                    if data == "print all".encode() or data == "1".encode():
                        print('Должны напечатать все книги')
                        msg = run(str(data.decode("utf-8")), listOfbooks, "")
                        ready[0][0].send(msg.encode())
                    if data == "count".encode() or data == "7".encode():
                        print("Подсчет числа книг")
                        msg = run(str(data.decode("utf-8")), listOfbooks, "")
                        ready[0][0].send(str(msg).encode())#Возращает число
                    if data == "exit".encode() or data == "5":
                        ready[0][0].send('okGoodbye'.encode())
                        #ready[0][0].close()
                        for j in range(len(conn)):
                            print('Сравниваем коннекшин ', j)
                            if conn[j] == ready[0][0]:
                                conn.pop(j)
                                print('Клиент ', j, ' Разорвал соединение')
                                print('Теперь количество клиентов: ', len(conn))
                                break
                    if data == "save".encode() or data == "8".encode():
                        print("Сохраняем файл")
                        msg = run("save", listOfbooks, "")
                        ready[0][0].send(str(msg).encode())
                    print('Пришло сообщение!')
                    print(data.decode())
                    #print('Отправляю клиенту: ', i)
                    #ans = "Ответ от сервака: ".encode() + data + "\n".encode()
                    #ready[0][0].send(ans)
                    data = 0
                ready = None
            except socket.error as e:
                if e.errno == 10053:
                    conn.pop(i)
                    print("Подключено пользователй:", len(conn))
                else:
                    raise

def Accepter():
    while 1:
        time.sleep(2)
        print('in accepter')
        global conn
        conn.append(sock.accept()[0])
        print("Подключено пользователй:", len(conn))


t11 = threading.Thread(target=SenderAndRecier)
t3 = threading.Thread(target=Accepter)

t11.start()
t3.start()