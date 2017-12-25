import socket
import threading
import sys

import time

import select

from appJson import run

sock = socket.socket()
sock.bind(('', 1080))
sock.listen(3)
#sock.setblocking(0)
conn = []
data = ''
listOfbooks = []
boolWasAddCommand = False
boolWasDeleteCommand = False
def SenderAndRecier():
    global data
    global conn
    global boolWasAddCommand
    global boolWasDeleteCommand
    while 1:
        print('in reciever')
        time.sleep(2)
        for i in range(len(conn)):
            print('слушаем клиента ', i)
            try:
                ready = select.select(list(conn), [], [], 4)
                print('Попытаемся получить сообщение 2')
                print(ready[0])
                print(conn[i])
                if ready[0]:
                    data = ready[0][0].recv(1024)
                    print('Клиент', i,  'активен. Получили сообщение.')
                if data:

                    if boolWasAddCommand:
                        print('Прошлая команда была: добавить книгу')
                        msg = run("add", listOfbooks, data.decode("utf-8"))
                        ready[0][0].send(msg.encode())
                        boolWasAddCommand = False
                    if boolWasDeleteCommand:
                        print('Прошлая команда была: удалить книгу')
                        msg = run("delete", listOfbooks, data.decode("utf-8"))
                        ready[0][0].send(msg.encode())
                        boolWasDeleteCommand = False
                    if data == "add".encode():
                        print('Мы должны добавить книгу в библиоткеу!')
                        boolWasAddCommand = True
                    if data == "delete".encode():
                        print('Мы должны удалить книгу из библиотеки')
                        boolWasDeleteCommand = True
                    if data == "print all".encode():
                        print('Должны напечатать все книги')
                        msg = run(str(data.decode("utf-8")), listOfbooks, "")
                        ready[0][0].send(msg.encode())
                    print('Пришло сообщение!')
                    print(data.decode())
                    print('Отправляю клиенту: ', i)
                    ans = "Ответ от сервака: ".encode() + data + "\n".encode()
                    ready[0][0].send(ans)
                    data = 0
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


# init threads
#t1 = threading.Thread(target=Reciver)
#t2 = threading.Thread(target=Sender)
t11 = threading.Thread(target=SenderAndRecier)
t3 = threading.Thread(target=Accepter)

# start threads
#t1.start()
#t2.start()
t11.start()
t3.start()