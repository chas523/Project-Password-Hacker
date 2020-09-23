# Project Password Hacker

## Stage 1/5:
## Objectives
*Your program will receive command line arguments in this order:*

1. IP address
2. port
3. message for sending

*The algorithm is the following:*

1. Create a new socket.
2. Connect to a host and a port using the socket.
3. Send a message from the third command line argument to the host using the socket.
4. Receive the server’s response.
5. Print the server’s response.
6. Close the socket.

## Examples

Example 1:
```cmd
python hack.py localhost 9090 password
Wrong password!
```
Example 2:
```cmd
python hack.py 127.0.0.1 9090 qwerty
Connection Success!
```
