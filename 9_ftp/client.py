import socket

host = '127.0.0.1'
port = 5555

s = socket.socket()
s.connect((host, port))


commands = {1: "get", 2: "put", 3: "pwd", 4: "ls", 5: "cd", 6: "quit"}
while True:
    print(commands)
    operation = int(raw_input("->Enter Command"))
    if(operation == 1):
        print("Get Operation")
        s.send(commands[operation])
        file_name = raw_input("Enter File Name")
        s.send(file_name)
        op = s.recv(8196)
        print op
        print "###########"
