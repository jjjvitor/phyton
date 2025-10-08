import os
os.system("cls")

# criando uma funcao
def converter_centimetros(numero):
    return numero * 100

# codigo principal
numero = int(input("digite um numero: "))
resposta = converter_centimetros(numero) # chamando a funcao
print(f"resultado: {resposta} centimetros.")
