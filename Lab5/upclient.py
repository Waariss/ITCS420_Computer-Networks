import socket
import time

sendtoserver = str(input("Enter two number: "))
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

msg = sendtoserver

client.sendto(sendtoserver.encode(), (socket.gethostname(), 2233))
data = client.recvfrom(1024)
t = time.localtime()
print("6388014: %s "% time.asctime(t), data[0].decode())

client.close()