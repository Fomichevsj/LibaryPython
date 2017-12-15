import socket
import threading
import sys

import time

sock = socket.socket()
sock.bind(('', 1080))
sock.listen(3)
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
                conn[i].send("Ответ от сервака".encode())
            data = 0

def Accepter():
    while 1:
        global conn
        conn.append(sock.accept()[0])
        print("Подключено пользователй:", len(conn))


# init threads
t1 = threading.Thread(target=Reciver)
t2 = threading.Thread(target=Sender)
t3 = threading.Thread(target=Accepter)

# start threads
t1.start()
t2.start()
t3.start()