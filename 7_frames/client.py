import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 2231))

while True:
    str1 = s.recv(1024)
    if(str1 == 'exit'):
        break
    print str1
    choice = input("if any error press 1 else press 0:")
    if(choice == 0):
        s.send('0')
        continue
    else:
        s.send('1')
        frameno = raw_input("enter the frame number:")
        print frameno
        s.send(frameno)
        continue
