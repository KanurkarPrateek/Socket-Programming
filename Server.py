import socket
import sys

s = socket.socket()

print("Socket Created")

port = 8080
s.bind(('', port))
print(f'socket binded succesfully {port}')

s.listen(6)
print("socket is listening")

while True:
    c , add = s.accept()
    print("got connection from add", add)
    msg = "thanks for connecting"
    c.send(msg.encode())
    c.close()

