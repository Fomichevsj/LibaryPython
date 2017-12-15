import socket
import threading
import sys

host = "localhost"
port = 1080
sock = socket.socket()
sock.connect((host, port))
def Reciver():
    while 1:
        data = sock.recv(1024)
        if data:
            print(data.decode())

def Sender():
    while 1:
        message = input()
        if message == "exit":
            sock.close()
            sys.exit()
        else:
            sock.send(message.encode())

# init threads
t1 = threading.Thread(target=Reciver)
t2 = threading.Thread(target=Sender)

# start threads
t1.start()
t2.start()