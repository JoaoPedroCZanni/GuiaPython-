import socket

# funcionalidade especifica para endereços de IP
resp="S"
while(resp=="S"):
    url = input("Digite uma url: ")
    ip=socket.gethostbyname(url)
    print("o IP referente a url informada é: ", ip)
    resp=input("Digite <s> para continuar: ").upper()
else:
    resp =="N";
    print("Vazando do sistema").upper()
