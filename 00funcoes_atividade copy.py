import os
import time

os.system("cls")

# criando uma funcao
def saudacao():
    print("boa tarde!")
    time.sleep(3) # espera 3 segundos.
    os.system("cls")
    return

# codigo principal
saudacao() # chamando funcao
print("exemplo de uso de uma duncao sem parametros")