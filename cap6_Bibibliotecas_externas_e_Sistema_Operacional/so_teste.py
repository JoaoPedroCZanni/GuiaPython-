import platform
import getpass
from datetime import datetime

# para ver coisas sobre a maquina
print("Nome maquina:..........", platform.node())
print("Arquitetura:..........", platform.architecture())
print("Sistema Operacional:..........", platform.system())
print("Versao do SO:..........", platform.release())
print("Processador:..........", platform.processor())
print("Versão do Python:..........", platform.python_version())

# para ver tudo no atual momento
print(datetime.now())

# para ver o usuario da maquina
usuario = (getpass.getuser())

# sistema para pedir uma senha para entrar, porem nao funciona pois tem que mudar o modo de exibicao do console "emulate terminal output console"
senha = (getpass.getpass("Digite sua senha:......"))

if usuario == 'user' and senha == 'hello':
    print('bem vindo ')
else:
    print('voce não tem acesso')