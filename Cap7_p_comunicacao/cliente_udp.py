# um cliente pode ser implemnetado para se conectar a um servidor e trocar dados

from socket import *

servidor = "127.0.0.1"
porta = 42210

obj_socket = socket(AF_INET, SOCK_DGRAM)

try:
    while True:
        mensagem = input("Sua mensagem: ")
        obj_socket.sendto(mensagem.encode(), (servidor, porta))

        # Aguardando resposta do servidor
        dados, origem = obj_socket.recvfrom(65535)
        print(f"Resposta do servidor: {dados.decode()}")

except Exception as e:
    print(f"Erro de conexão: {e}")

finally:
    obj_socket.close()
