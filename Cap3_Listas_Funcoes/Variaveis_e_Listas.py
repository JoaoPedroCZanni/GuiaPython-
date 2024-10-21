# inventario
inventario=[]
resposta = "S"

while resposta =="S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()


# essa segunda parte é para imprimir os dados na tela
for elemento in inventario:
    print (elemento)