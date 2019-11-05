# Funcionamiento Basico

- Se establecen un servidor que escucha a conexiones entrantes en el puerto 5000. 
- El servidor recibe datos en forma de cadenas de caracteres, y termina la conexión cuando recibe una cadena     igual a “chau”.
- El cliente se conecta al socket servidor, y ejecuta un comando input para ingresar texto por consola que       será convertido a bytes y enviado al servidor. 
- Al recibir el mensaje el servidor lo muestra por consola y abre un prompt para contestar al cliente, estos     intercambios de mensajes se hacen hasta que el cliente envíe la cadena “chau” al servidor.
