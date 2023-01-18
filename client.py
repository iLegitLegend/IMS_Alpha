import socket
import logging
import threading
def readincomingtext(name):
    while True:
        data = s.recv(buffer_size)
        data = data.decode()
        print("\n")
        logging.info("%s From Host: " + data, name)
host = "Lab120-05"
port = 9440
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
x = threading.Thread(target=readincomingtext, args=('Message',), daemon=True)
x.start()
print("Type a message, or [close] to disconnect.")
while True:
    text = input().encode("utf-8")
    if text.decode() == "[close]":
        s.send(("The client has closed the application.").encode("utf-8"))
        break
    s.send(text)
s.close()
