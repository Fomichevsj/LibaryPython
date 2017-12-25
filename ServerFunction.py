import socket

from appJson import run

def server():
    print("стартуем сервер")
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(2)
    conn, addr = sock.accept()

    print('connected:', addr)
    listOfbooks = []
    while True:
        data = conn.recv(1024)
        print(data)
        if not data:
            print("not data")
            break
        if data == b"add":
            print("будем добавлять книгу. Все данные у клиента уже подготовленны")
            paramsstr = conn.recv(1024)
            paramsstr = str(paramsstr, "utf-8")
            msg = run(str(data.decode("utf-8")),listOfbooks, paramsstr)
            conn.send(bytearray(msg,"utf-8"))
            continue
        elif data == b"delete":
            print("Будем удалять кигу по имени")
            paramsstr = conn.recv(1024)
            paramsstr = str(paramsstr, "utf-8")
            msg = run(str(data.decode("utf-8")), listOfbooks, paramsstr)
            print("msg from app ", msg)
            conn.send(bytearray(msg, "utf-8"))
        elif data == b"find":
            print("Будем искать кигу по имени")
            paramsstr = conn.recv(1024)
            paramsstr = str(paramsstr, "utf-8")
            msg = run(str(data.decode("utf-8")), listOfbooks, paramsstr)
            print("msg from app ", msg)
            conn.send(bytearray(msg, "utf-8"))
        else:
            msg = run(str(data.decode("utf-8")), listOfbooks, "")
            if msg == "no such command":
                conn.send(b"no such command")
            print("msg from func: ", msg)
            conn.send(bytearray(str(msg), "utf-8"))


    conn.close()