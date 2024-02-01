import socket

HOST = 'localhost'
PORT = 5050

DISCONNECT_MESSAGE = 'DISCONNECT!'

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

CLIENT.connect((HOST, PORT))

print('=' * 55)
print('type [C] to close the connection')

while True:
    try:
        print('=' * 55)
        msg = str(input('type a mathematical expression to calculate: '))
        print('=' * 55)

        if msg.upper() == 'C':
            CLIENT.sendall(DISCONNECT_MESSAGE.encode())
            CLIENT.close()

            print('Connection closed...')
            print('=' * 55)

            break
        else:
            CLIENT.sendall(msg.encode())
        
        print(CLIENT.recv(1024).decode())       
    except Exception as err:
        print(f'[EXCEPTION] {err}')
        print('=' * 55)