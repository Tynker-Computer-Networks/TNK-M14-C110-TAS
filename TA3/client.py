import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000
nickname = input("Choose your nickname: ")

client.connect((ip_address, port))
print("Connected with the server...")

# Create a receive() function
def receive():
    # Create an infinite loop
    while True:
        # write try block
        try:
            # indent following lines to be part of the while loop
            message = client.recv(2048).decode('utf-8')
            # line already present in boiler
            print("Message from server: ", message)
        # Add except 
        except:
            # Print An error occurred!
            print("An error occurred!")
            # Close the client socket
            client.close()
            # Break the loop 
            break
        

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

# Create a thread receive_thread that runs receive function
receive_thread = Thread(target=receive)
# Start the receive_thread
receive_thread.start()


write_thread = Thread(target=write)
write_thread.start()