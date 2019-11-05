
import socket


def client_program():
    host = socket.gethostname()  # De esta forma se busca el nombre del host en el socket ya que es la misma computadora
    port = 5000  # Puerto para establecer el socket

    client_socket = socket.socket()  # Inicializa el socket
    client_socket.connect((host, port))  # Se conecta al servidor por el socket

    mensaje = input(" -> ")  # De esta forma se indica la simboligia para identificar quien escribe

    while mensaje.lower().strip() != 'chau': # Verifica que el mensaje no sea chau, sino cierra la conexion
        client_socket.send(mensaje.encode())  # Envia el mensaje que se escriba
        data = client_socket.recv(1024).decode()  # Recibe el mensaje que se haya enviado del servidor

        print('Recibido desde el servidor: ' + data)  # Muestra el mensaje en la terminal

        mensaje = input(" -> ")  # Vuelve a permitir escribi un nuevo mensaje

    client_socket.close()  # Cierra el socket


if __name__ == '__main__': # Main que se ejecuta en primera instancia y llama al cliente
    client_program()
