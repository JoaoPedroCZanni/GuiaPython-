# um servidor pode ser criado para escutar conexões de clientes, processar dados e enviar respostas

from socket import *


servidor="127.0.0.1"
porta = 42210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((servidor,porta))
print("Servidor pronto........ ")

while True:
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem..........: ", origem)
    print("Dados Recebidos..........: ", dados.decode())
    resposta=input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem)

obj_socket.close()