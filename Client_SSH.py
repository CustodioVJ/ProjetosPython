import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    client.connect(("127.0.0.1", 7755))
    client.send(b"Eae jovem\n")
    response = client.recv(1824).decode()
    print(response)
except Exception as error:
    print("Something went wrong!")

#client para tcp