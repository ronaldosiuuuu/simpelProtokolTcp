from socket import *
from threading import *
from random import *


serverPort = 12001

def handleClient(clientSocket, addr):
    sentence = clientSocket.recv(2048).decode()
    splittetText = sentence.split()
    Text=''
    tal1 = int (splittetText[1])
    tal2 = int (splittetText[2])
    if(splittetText[0].lower() == 'sub'):
        Text = f'{tal2} - {tal1} = {(tal2 - tal1)}'
    
    elif(splittetText[0].lower() == 'add'):
         Text = f'{tal1} + {tal2} = {(tal1 + tal2)}'
    
    elif(splittetText[0].lower() == 'random'):
         Text = f'{randint(tal1, tal2)}'

    else:
        Text = f'Prøv igen {splittetText[0]}'
    
    clientSocket.send(Text.encode())
    clientSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Serveren er klar til brug', serverSocket)


while 1:
        connectionSocket, addr = serverSocket.accept()
        print('Forbindelse oprettet', addr)
        Thread(target=handleClient, args=(connectionSocket, addr)).start()
