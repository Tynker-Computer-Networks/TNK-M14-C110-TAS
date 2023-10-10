import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000
# get nickname from console input
nickname = input("Choose your nickname: ")

client.connect((ip_address, port))

print("Connected with the server...")

message = client.recv(2048).decode('utf-8')

print("Message from server: ", message)

# Get nickname into message variable
message = nickname

# Send the encoded message using send method
client.send(message.encode('utf-8'))