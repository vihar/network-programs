import socket
s = socket.socket()
s.bind(('127.0.0.1', 2220))
s.listen(1)
ipmac = {
    "10.1.1.8": "44:dd:22:11:33",
    "127.0.0.1": "33:aa:fe:4e:2d",
    "10.1.8.5": "23:a3:5d:33:9d"
}

client, address = s.accept()

str = client.recv(1024)
out = ipmac[str]

client.send(out)

str = client.recv(1024)
for k in ipmac.keys():
    if ipmac[k] == str:
        client.send(k)
s.close()
