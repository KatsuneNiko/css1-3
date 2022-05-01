from socket import *

def check_luhn(card_no):
    n_digits = len(card_no)
    n_sum = 0
    is_second = False

    for i in range(n_digits - 1, -1, -1):
        d = ord(card_no[i]) - ord('0')

        if is_second:
            d = d * 2

        n_sum += d // 10
        n_sum += d % 10

        is_second = not is_second

    if n_sum % 10 == 0:
        return True
    else:
        return False

serverPort = 80
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Host server ready.")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    decoded_message = message.decode()
    if check_luhn(decoded_message):
        serverSocket.sendto("True".encode(), clientAddress)
        print("Credit card number correct. Verification complete.")
        break
    else:
        serverSocket.sendto("False".encode(), clientAddress)
        print("Credit card number incorrect. Verification incomplete.")
        print("Waiting for client...")