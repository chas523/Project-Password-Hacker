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
