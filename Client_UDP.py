import socket

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.sendto((b"Message"), "127.0.0.1", 5544)
    data, sender = client.recvfrom(1902)
    print(sender[0] + ": " + data.encode())
except Exception as error:
    print("Something went wrong")
    print(error)

#Client UDP