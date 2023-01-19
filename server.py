import logging
import threading
import socket
def readincomingtext(name):  #the function that the thread will run until the code ends
    while True:
        data = client.recv(buffer_size)
        data = data.decode()
        logging.info("s% i - From Client: " + data, name)
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer_size = 1024
mysocket.bind((socket.gethostname(), 9447))
mysocket.listen()
(client, (ip, port)) = mysocket.accept()
client.send(b"Connection with Server Established")
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
x = threading.Thread(target=readincomingtext, args=(1,), daemon=True)
x.start()
print("What would you like to send?(or enter [close] if you want to stop messaging:")
print("\n")
while True:
    message = input().encode("utf-8")
    if message.decode() == "[close]":
        break
    client.send(message)
mysocket.close()
