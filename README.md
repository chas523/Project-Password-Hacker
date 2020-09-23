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
code: 
```python
import sys
import socket



if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Wrong input")
    else:
        with socket.socket() as client_socket:
            try:
                port = int(args[2])
                host_name = args[1]
                password = args[3]
            except:
                print("Wrong input")
            client_socket.connect((host_name,port))
            password = password.encode()
            client_socket.send(password)
            response = client_socket.recv(1024)
            response = response.decode()
            print(response)

    pass
 ```
