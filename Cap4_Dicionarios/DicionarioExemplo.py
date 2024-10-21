# 1° teste
usuarios  = {}
print(usuarios)

#  2° teste
usuarios = {"chaves" : ["Chaves do 8","24/12/2017" , "recep_01" ],
            "quico": ["Quico das Flores do dia", "20/12/2017","Raiox_03"]
}
print(usuarios)

# colocando um novo registro dentro do dicionario
usuarios ["Florinda"] = ["Dona Florinda", "24/12/2017" , "Raiox_01"]
print(usuarios)

# resgatando uma informação do dicionario e apresentando ao usuario
print("###----###")
print(usuarios.get("quico"))