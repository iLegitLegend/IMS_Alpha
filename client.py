import socket
import logging
import threading
def readincomingtext(name):
    while True:
        data = s.recv(buffer_size)
        data = data.decode()
        logging.info("s% i - From Host: " + data, name)
host = "DESKTOP-IK94OT8"
port = 9447
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
x = threading.Thread(target=readincomingtext, args=(1,), daemon=True)
x.start()
print("Enter a message, or [close] to break connection.\n")
print("\n")
while True:
    text = input().encode("utf-8")
    if text.decode() == "[close]":
        s.send(("The client has closed the application.").encode("utf-8"))
        break
    s.send(text)
s.close()
