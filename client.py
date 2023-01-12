import socket
host = 'Lab120-04'
port = 9440
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    data = s.recv(buffer_size)
    print("received data:", data.decode())
    text = input("input message here:")
    text = text.encode('utf-8')
    s.send(text)
    breakoff = input("would you like to stop sending and receiving messages? (yes or no): ")
    if breakoff.lower() == "yes":
        break
s.close()
