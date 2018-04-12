import socket

host = '127.0.0.1'
port = 2222

s = socket.socket()
s.bind((host, port))
s.listen(1)

client, addr = s.accept()

while(True):
    data = client.recv(1024)
    client.send(data)

s.close()
