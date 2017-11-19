import socket

import time

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
    print("Введите комманду")
    cmd = input()
    if cmd == "exit":
        sock.send(b"exit")
        sock.close()
        exit(0)
    if cmd == "add":
        print("Введите необходимые данные для книги", end="\n")
        print("\tВведите название книги: ", end='')
        name = input()
        print("")
        print("\tВведите автора книги: ", end='')
        author = input()
        print("")
        print("\tВведите год издания книги: ", end='')
        try:
            date = int(input())  # TODO нужно учесть, что формат может быть не тот
        except ValueError:
            print("Дата может быть только числом. Попробуйте заново.")
            break
        print()
        print("\tВведите издательский дом: ", end='')
        publis_house = input()
        sock.send(b"add")
        res = name + " " + author + " " + str(date) + " " + publis_house
        sock.send(bytearray(res,"utf-8"))
        #sock.send(bytearray(name,'utf-8'))
        #sock.send(bytearray(author, 'utf-8'))
        #sock.send(bytearray(str(date), 'utf-8'))
        #sock.send(bytearray(publis_house, 'utf-8'))
    else:
        print("отправляем команду")
        sock.send(bytearray(cmd, "utf-8"))
        data = sock.recv(100*1024)
        print("ответ от сервера ",str(data, "utf-8"))
sock.close()
print(data)