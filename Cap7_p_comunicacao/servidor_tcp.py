# o socket é o ponto de comunicação entre dois computadores em uma rede permitindo a troca de dados entre eles

from socket import *

servidor ="127.0.0.1"
porta=41210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor,porta))
obj_socket.listen(2)

print("Aguardando cliente...")

while True:
    con,cliente = obj_socket.accept()
    print("Conectando com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Ola Cliente'
        con.send(msg_enviada)
        break
    con.close()