import socket
import threading
import time
import sys

#**************************************************************************************************************
#  Cuando se ejecute el programa, hay que pasar como parametro la ip y el puerto del servidor.
#**************************************************************************************************************

def hilo(c,conectadosNombre,conectadosSockets):
    nombre = threading.current_thread().name
    while True:
        # datos recibidos de un cliente
        data = c.recv(1024)
        if not data:
            print(nombre+' ha cerrado la sesión')
            break
        contestacion='<'+nombre+'>'+ data.decode()
        print('<',nombre,'>', data.decode())
        data=str(contestacion)
        # Enviamos los datos al cliente
        for i in conectadosSockets:
            i.send(contestacion.encode())
        #time.sleep(0.5)
    c.close() # Cerramos la conexión

def Main(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print('Habilitamos el socket en el puerto', port)
    s.listen()
    print('Servidor preparado y a la escucha...')
    conectadosNombre=[]
    conectadosSockets=[]
    while True:
        # Acepta conexion del cliente
        c, addr = s.accept()
        data = c.recv(1024)
        info=data.decode()
        info= info.split('/')
        nombre=info[0]
        conectadosNombre.append(nombre)
        conectadosSockets.append(c)
        print(nombre," se ha conectado al chat")
        h = threading.Thread(name=nombre, target=hilo, args=(c,conectadosNombre,conectadosSockets,))
        h.start()
    s.close()

if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    Main(str(host),port)