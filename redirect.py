#!/usr/bin/python3
#LAURA TRABAS CLAVERO

import socket
import random

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        peticion = recvSocket.recv(2048).decode("utf-8", "strict")
        print(peticion)
        URL = str(random.randint(0, 10000000000000000000))
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                              "<html><body><h1>" +
                              "<meta http-equiv='refresh' content= 4;url=/" +
                              URL + "/>Redirigiendo a... /" +
							  URL + "</h1></body></html>"
                              "\r\n", "utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
mySocket.close()
