# esse codigo vai dar erro pois não tenho importado o conjunto de dados especificado
# este esta no seguinte link: https://archive.ics.uci.edu/dataset/53/iris

basedados =[]
with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(","))

print(basedados)
print (basedados[0][0] + basedados[0][1])