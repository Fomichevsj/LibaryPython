import socket
import threading
import sys

import time

import select

sock = socket.socket()
sock.bind(('', 1080))
sock.listen(3)
#sock.setblocking(0)
conn = []
data = ''
def Reciver():
    global data
    while 1:
        print('in reciever')
        time.sleep(2)
        for i in range(len(conn)):
            try:
                data = conn[i].recv(1024)
                if data:
                    print('Пришло сообщение!')
                    print(data.decode())
            except socket.error as e:
                if e.errno == 10053:
                    conn.pop(i)
                    print("Подключено пользователй:", len(conn))
                else:
                    raise

def Sender():
    while 1:
        print('in sender')
        time.sleep(2)
        global conn
        global data
        #message = input()
        if data:
            for i in range(len(conn)):
                print('Отправляю клиенту: ', i)
                ans = "Ответ от сервака: ".encode() + data
                conn[i].send(ans)
            data = 0

def SenderAndRecier():
    global data
    global conn
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
                    print('Пришло сообщение!')
                    print(data.decode())
                    print('Отправляю клиенту: ', i)
                    ans = "Ответ от сервака: ".encode() + data
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