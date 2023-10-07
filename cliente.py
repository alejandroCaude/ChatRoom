import socket
import threading
import sys

#**************************************************************************************************************
#  Cuando se ejecute el programa, hay que pasar como parametro la ip, el puerto del servidor, y el nombre de chat.
#**************************************************************************************************************
def recibir(s):
    while True:
        data = s.recv(1024)
        # El servidor devuelve reverse string
        print(str(data.decode()))

def enviar(s):
    while True:
        message = input(" ")
        s.send(message.encode())
        if True:
            message = input(" ")
            continue
        

def Main(host, port,nombre):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # Conectado al servidor
    s.connect((host,port))
    #Envio el nombre del cliente al servidor
    info= nombre + "/"+ str(s)
    s.send(info.encode())
    # Escribir la frase a enviar
    print("*********************")
    print("CHAT EN TIEMPO REAL")
    print("*********************")
    h = threading.Thread(name=nombre, target=recibir, args=(s,))
    h.start()
    j = threading.Thread(name=nombre, target=enviar, args=(s,))
    j.start()
# S cierra la conexión
   # s.close()
if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    nombre = sys.argv[3]
    Main(str(host),port,str(nombre))
  