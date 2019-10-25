
import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    mensaje = input(" -> ")  # take input

    while mensaje.lower().strip() != 'chau':
        client_socket.send(mensaje.encode())  # send mensaje
        data = client_socket.recv(1024).decode()  # receive response

        print('Recibido desde el servidor: ' + data)  # show in terminal

        mensaje = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
