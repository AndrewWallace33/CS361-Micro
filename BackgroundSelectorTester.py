# Andrew Wallace
# CS361
# The purpose of this file is to server as a dummy connection point to background selector.
# To run for testing and see the implementation.

from socket import *

# Set up the variables to connect on the port.
hostname = '127.0.0.1'
port_num = 2554

# Ask for input.
number = input("Enter a positive value greater than 0: ")

# Create the connection socket.
with socket(AF_INET, SOCK_STREAM) as sock:
    sock.connect((hostname, port_num))
    # Encode and send the value
    sock.send(number.encode())
    # Receive the value back and decode it
    response = sock.recv(4096).decode()
    # Print value and close the socket.
    print("Returned Value: " + response)
    sock.close()
