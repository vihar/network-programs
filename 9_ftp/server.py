import socket
import os

host = '127.0.0.1'
port = 5555

s = socket.socket()
s.bind((host, port))
s.listen(1)
client, address = s.accept()

while True:
    k = client.recv(1024)
    if k == 'get':
        name = client.recv(1024)
        os.system('cat ' + name + '.txt')
        file = open('out.txt', 'r')
        out = ' '
        for l in file:
            out += l
        client.send(out)
        file.close()
