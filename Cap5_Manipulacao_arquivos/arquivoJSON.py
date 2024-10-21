# importa o json porém com erro, o exemplo da aula utiliza o modo "r"

import json

with open("bd.json", "a") as arq_json:
    dicionario =  json.load(arq_json)
    print(dicionario)
