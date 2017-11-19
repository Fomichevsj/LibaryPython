import socket

from appJson import run

def startServer():
    #Далее, внутри функции run("hello") мы заменим взаимодействие в консоли на взаимоодействие через сокеты
    #Пока оставим так
    print("Сервер запущен")
    sock = socket.socket()#Создаем сокет
    sock.bind(('',9090))#выбираем хост и порт
    sock.listen(1)# устанавливаем размер очередни
    conn, addr = sock.accept()#новый сокет и адрес клиента
    while True:
        data = conn.recv(1024)
        if not data:
            break
        run("hello")
        conn.send(data.upper())
    conn.close()