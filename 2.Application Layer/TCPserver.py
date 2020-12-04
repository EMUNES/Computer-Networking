from socket import *

# set up welcome socket port
serverPort = 12000

# set up the socket on port 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

# listen to message
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    # get the assigned socket and address for the connection server
    connectionSocket, addr = serverSocket.accept()

    # receive the message from the port and transfer it into uppercase
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    
    # dump the message into the pipe
    connectionSocket.send(capitalizedSentence.encode())
    
    connectionSocket.close()