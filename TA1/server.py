import socket
# Import Thread
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

clients = []

print("Server has started...")

# Define clientThread method
def clientThread(conn, addr):
    
    conn.send("Welcome to this chatroom!".encode('utf-8'))

    # Create an infinite loop
    while True:
        # Create a try block
        try:
            # Receive the message on the connection i.e. "conn" and store it in message variable
            message = conn.recv(2048).decode('utf-8')
            # Check if message exits
            if message:
                # Print the message
                print("Message from client: ", message)
        # Create except block
        except:
            # Continue the loop 
            continue

while True:
    conn, addr = server.accept()
    
    print("New Client Connected", addr[0])
    clients.append(conn)

    # Move this line to the clientThread method
    # conn.send("Welcome to this chatroom!".encode())
    
    # Create a new thread with clientThread as target and conn, addr as args
    new_thread = Thread(target= clientThread,args=(conn, addr))
    # start the new thread
    new_thread.start()
