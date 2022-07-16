import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
# well just because I use same computer
# change it to fxed one
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    # b' ' blank byte spaces
    # to send exactly 64 bytes
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    # handle the msg we send back size

send("Hello World!")
input()  # click enter to run the next line
send("Hello Everyone!")
input()
send("Hellow Wass")
# sending from different prompt makes new connections
send(DISCONNECT_MESSAGE)
