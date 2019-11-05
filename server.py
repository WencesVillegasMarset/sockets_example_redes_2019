
import socket


def server_program():
    host = socket.gethostname() # De esta forma se busca el nombre del host en el socket ya que es la misma computadora
    port = 5000  # Puerto para establecer el socket

    server_socket = socket.socket()  # Inicializa el socket
    server_socket.bind((host, port))  # Se conecta al servidor por el socket

    # Configura cuantos clientes se puede escuchar simultaneamente
    server_socket.listen(2)
    conn, address = server_socket.accept()  # Acepta una nueva conexion, la cual se establecio el en cliente
    print("Conectado desde: " + str(address)) # Muestra desde donde se realiza la conexion
    while True:
        # Recibe la informacion que se envia. Se indica que no recibe data mas grande de 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Usuario conectado: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # Permite enviar datos al cliente

    conn.close()  # Cierra el socket


if __name__ == '__main__': # Main que se ejecuta en primera instancia y llama al cliente
    server_program()
