import socket
import threading

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 21948       # Port to listen on (non-privileged ports are > 1023)

HEADER_LENGTH = 100
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


def start() :
    print(f"Server start at port {PORT}")
    print("---------------------------")
    server.listen()

    while True:
        conn, addr = server.accept()
        
        thread = threading.Thread(target=handle_join, args=(conn, addr))
        thread.start()

def handle_join(conn, addr) :
    print(f"New ip {addr[0]} join!")

    conn.send("---------------------Welcome to chat room!---------------------".encode(FORMAT))

    connecting = True

    while connecting :
        try :
            msg = conn.recv(HEADER_LENGTH)
            if msg :
                msg = f"[{addr[0]}] : {msg.decode(FORMAT)}" 
                print(msg)
                show_message(msg, conn)
        except :
            pass

def show_message(msg, conn) :
    conn.send(msg.encode(FORMAT))

start()
