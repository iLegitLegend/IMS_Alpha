import logging
import threading
import socket
def readincomingtext(name):
    while True:
        data = client.recv(buffer_size)
        data = data.decode()
        print("\n")
        logging.info("%s From Client: " + data, name)

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer_size = 1024
text = "no"
mysocket.bind((socket.gethostname(), 9440))
mysocket.listen()
(client, (ip, port)) = mysocket.accept()
client.send(b"Connection with Server Established")
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
x = threading.Thread(target=readincomingtext, args=('Message',), daemon=True)
x.start()
print("Type a message, or [close] to disconnect.")
while True:
    message = input().encode("utf-8")
    if message.decode() == "[close]":
        break
    client.send(message)
mysocket.close()



