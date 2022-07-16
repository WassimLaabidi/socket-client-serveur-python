import socket
import threading

""" thread more than 1 struct in one time not wait a code to finish before execute open more than 1 session maybe"""

HEADER = 64
PORT = 5050
# SERVER = "192.168.1.168"
# static address
SERVER = socket.gethostbyname(socket.gethostname())
# Dynamic address
# print(SERVER)
# print(socket.gethostname())

ADDR = (SERVER, PORT)
# const in uppercase
# bind socket to specific addr needs to be in tuple

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# when we receive the msg we close the connection between client and server

# open up the device for their connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# what type of address we're locking for (accepting for specific connections)
# streaming data through socket
# different way through sending sockets

server.bind(ADDR)


def handle_client(conn, addr):
    # handle all communications between the clients and server
    # handle 1 client and 1 server
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # when the msg is sent we have to code it
        # not pass the line until we receive a msg from our client
        # not block other client for connection
        # wait until something sends
        # enters how many bytes to except
        if msg_length:  # not none
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            # How long the msg is coming
            # how many bytes we're receiving
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    # close connection
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # store conn -> socket object allow us to communicate back, addr -> IP add + port
        # handle new cnx distribute it
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        # how many threads are active, amount of clients connected
        # new thread for each client, subtract server thread


# start function
print("[STARTING] server is starting...")
start()
