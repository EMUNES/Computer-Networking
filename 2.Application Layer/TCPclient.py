from socket import *

# configure server info
serverName = 'servername'
serverPort = 12000

# create TCP client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# create a connection to the server
clientSocket.connect((serverName, serverPort))

# get use input
sentence = input('Input lowercase sentence:')

# send message - just through things in the pipe 
# which means no need to specify server info 
clientSocket.send(sentence.encode())

# receive message from server
modifiedSentence = clientSocket.recv(1024)

print('From Server:', modifiedSentence)

clientSocket.close()