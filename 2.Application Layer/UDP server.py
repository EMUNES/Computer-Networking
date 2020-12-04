from socket import *
serverPort = 12000

# create an UDP server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# binds the port number 12000 to the server's socket
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

# an always-on server
while True:
    # receive the message and get the client address along with it 
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()

    # send back the modified message
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
