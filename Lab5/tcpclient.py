import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.connect(('127.0.0.1', 41111))

msg = input("Enter two number")
t = time.localtime()

client.send(msg.encode('ascii'))
data = client.recv(1024)
print ("6388014 : %s" %time.asctime(t), data.decode())
client.close()