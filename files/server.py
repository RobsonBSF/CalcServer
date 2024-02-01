import socket
import threading

HOST = 'localhost'
PORT = 5050

DISCONNECT_MESSAGE = 'DISCONNECT!'

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected!')
    print('=' * 55)

    while True:
        try:
            msg = conn.recv(1024).decode('utf-8')

            if msg == DISCONNECT_MESSAGE:
                print(f'[SERVER] {addr} disconnected...')
                print('=' * 55)

                conn.close()
                break
            elif msg:
                ret_msg = f'{msg} = {eval(msg)}'
                conn.sendall(str(ret_msg).encode())

        except Exception as err:
            conn.sendall(f'[EXCEPTION] {err}'.encode())
            print('=' * 55)
        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SERVER:

    SERVER.bind((HOST, PORT))
    SERVER.listen()

    print('=' * 55)
    print(f'[SERVER] listening on {HOST}:{PORT}')
    print('=' * 55)

    while True:
        conn, addr = SERVER.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()