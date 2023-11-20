# Andrew Wallace
# CS361
# The Purpose of this program is to run as a microservice which takes in a number.
# And returns a randon number within that range to be used to select a background image for
# The games main screen. This will be accomplished using python sockets and a TCP connection.

from socket import *
import random

# Setup the variables to connect on the port.
hostname = '127.0.0.1'
port_num = 2554

# Create and Bind socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((hostname, port_num))
# Listen for connections with a backlog of 1.
server_socket.listen(1)
# Listen until killed.
while True:
    # Accept the connection and block until data is sent.
    conn_socket, address = server_socket.accept()
    provided_string = conn_socket.recv(4096).decode()
    # Try to cast the string to an int - if error it will return -1.
    try:
        provided_number = int(provided_string)
    except ValueError:
        provided_number = -1

    # generate a random # to return - return -1 if the input was invalid.
    if provided_number > 0:
        random_int = random.randint(1, provided_number)
    else:
        random_int = -1
    # Send the data back and close the connection.
    conn_socket.send(str(random_int).encode())
    conn_socket.close()


