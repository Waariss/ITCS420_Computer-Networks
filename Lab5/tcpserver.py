import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',41111))
print("Waiting for connection...")
server.listen(5)
while True:
        client, addr=  server.accept()
        print("Received a connection from %s" % str(addr))
        data = client.recv(1024)
        split = data.split()
        x = int(split[0])
        y = int(split[1])
        print ("6388014: "+ str(x) + " " + str(y))
        sendclient = x +y 
        msg = str(sendclient)
        client.send(msg.encode())
        client.close()
        server.close()