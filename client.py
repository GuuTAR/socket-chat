import socket
import threading

PORT = 21948       # Port to listen on (non-privileged ports are > 1023)

HEADER_LENGTH = 100

FORMAT = "utf-8"

def send_msg() :
    while True :
        msg = str(input())
        client.send(msg.encode(FORMAT))

def recv_msg() :
    while True :
        message = client.recv(HEADER_LENGTH)
        if message :
            print(message.decode(FORMAT))

server_ip = input("Please insert server IP : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, PORT))

send_msg_thread = threading.Thread(target=send_msg)
send_msg_thread.start()

recv_msg_thread = threading.Thread(target=recv_msg)
recv_msg_thread.start()