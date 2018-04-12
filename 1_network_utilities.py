import socket
n = 0x56AB
print(n)
k = socket.htons(n)
print(k)
k = socket.ntohs(k)
print(k)
