import os
os.system("cls")

def calcular_soma(n1, n2):
    soma = (n1 + n2)
    print(f"soma: {soma}")
    return soma

def calcular_subtracao(n1, n2):
    subtracao = (n1 - n2)
    print(f"subtracao: {subtracao}")
    return subtracao

def calcular_multiplicacao(n1, n2):
    multiplicacao = (n1 * n2)
    print(f"multiplicacao: {multiplicacao}")
    return multiplicacao

def calcular_divisao(n1, n2):
    divisao = (n1 / n2)
    print(f"divisao: {divisao}")
    return divisao


primeiro_numero = int(input("digite um numero: "))
segundo_numero = int(input("digite um numero: "))


soma = calcular_soma(primeiro_numero, segundo_numero)
subtracao = calcular_subtracao(primeiro_numero, segundo_numero)
multiplicacao = calcular_multiplicacao(primeiro_numero, segundo_numero)
divisao = calcular_divisao(primeiro_numero, segundo_numero)