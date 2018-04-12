import socket

host = '127.0.0.1'
port = 2222

s = socket.socket()
s.connect((host, port))

n = 3


for i in range(0, n):
    data = raw_input()
    s.send(data)
    i = s.recv(1024)
    print i
