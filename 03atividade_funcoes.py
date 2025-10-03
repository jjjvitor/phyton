import os
os.system("cls")

# funcao com passagem de parametros
# criando uma fufncao
def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

print("solicitando dados")
numero = int(input("digite um numero: "))

# chamando a funcao
print("\nexibindo resultados")
tabuada(numero)