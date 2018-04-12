import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 2231))

s.listen(5)

input = raw_input("Enter the data to be transmitted : ")
client, address = s.accept()
print "Sending frames to :" + str(address)
window = 4
frames = []
for k in input:
    frames.append(k)
print frames

count = 0

while True:
    if len(input) - count > 4:
        window = 4

    else:
        window = len(input) - count

    if window <= 0:
        break

    temp = []

    for l in range(count, count + window):
        temp.append(str(l))

    client.send(''.join(frames[count:count + window]) + ' ' + ' '.join(temp))
    recv = client.recv(1024)

    if(int(recv) == 0):
        count += window
        continue
    else:
        frameno = client.recv(1024)
        frameno = int(frameno)
        print frameno
        client.send(
            ''.join(frames[frameno:count + window]) + ' ' + ' '.join(
                temp[frameno:]))
        count += window

client.send("exit")
s.close()
