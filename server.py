__author__ = "evfairchild"

import socket
import threading

HEADER = 64     # bytes
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "73.223.126.76"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # blocking line, will not continue until something is received form the client

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            # message protocol: first message will always be of length HEADER.
            # The client will respond with the length of the incoming message

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))    # send message to the client

    conn.close()


def start():
    """Handles new connections"""
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()    # blocking line, will not continue until a new connection is made
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
