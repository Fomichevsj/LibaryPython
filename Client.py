import socket

import time

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
    print("Введите комманду")
    cmd = input()
    if cmd == "exit":
        sock.close()
        exit(0)
    else:
        print("отправляем команду")
        sock.send(bytearray(cmd, "utf-8"))
        data = sock.recv(1024)
        print("ответ от сервера ",data)
sock.close()
print(data)