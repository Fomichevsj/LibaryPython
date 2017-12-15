import socket
print("след сокет")
sock1 = socket.socket()
sock1.bind(('', 9090))
sock1.listen(2)
conn1, addr1 = sock1.accept()
print("след сокет")
sock2 = socket.socket()
sock2.bind(('', 9090))
sock2.listen(2)
conn2, addr2 = sock2.accept()

print('connected:', addr1)
print('connected:', addr2)
