import os
os.system("cls")

def positivo_negativo(numero):
    if numero >= 0:
        print("o numero e positivo")
    else:
        print("o numero e negativo")

numero = float(input("digite o numero: "))

positivo_negativo(numero)