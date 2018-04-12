import socket
s = socket.socket()
s.connect(('127.0.0.1', 2220))

input = raw_input("Enter ip address:")
s.send(input)

k = s.recv(1024)
print "Mac address is : " + k
input = raw_input("Enter mac address:")
s.send(input)
k = s.recv(1024)
print "Ip address is : " + k
s.close()
