from socket import *

serverName = '192.168.1.109'
serverPort = 80
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Input credit card number: ')
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    incomingMessage, serverAddress = clientSocket.recvfrom(2048)
    if incomingMessage.decode() == "True":
        print("Credit card number correct. Verification complete.")
        break
    else:
        print("Credit card number incorrect. Please try again.")
clientSocket.close()