# CS361-Micro
Microservice for my partners CS361 Project

# Run the Microservice
Open up a standalone terminal window and run BackgroundSelector.py in it. After that the server will be good to go.

# Request Data
From your program connect to the socket with the following info over a TCP connection:

hostname = localhost

portnumber = 2554

```my_socket.connect((hostname, portnumber))```

Once connected send an integer value corresponding to the number of available background images you have (1 indexed - I.E you will never have 0 returned).

```my_socket.send(str(number_of_backgrounds).encode())```

Data has now been sent to server for processing.

# Recieve Data

To recieve data - have your same socket from above set the value of a recv call to a variable. The below will return a string corresponding to randomly selected image number.

```
response = my_socket.recv(4096).decode()
image_number = int(response)
```

# Error Handling
Server side if there is any issues or if an invalid integer is passed to the server (a number less than or equal to 0) the return value will be sent as a -1. So be sure to handle the -1 with a default fall back value.
