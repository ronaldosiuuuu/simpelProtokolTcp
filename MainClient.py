from socket import * 

serverName = 'localhost'
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
sentence = input('Vælg mellem et af følgende: add / sub / random ')

data = sentence.encode()
clientSocket.send(data)

datatilbage = clientSocket.recv(2048)
sentenceTilbage = datatilbage.decode()

print('Svar', sentenceTilbage)
clientSocket.close()