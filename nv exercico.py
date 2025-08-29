import os
os.system("cls")

primeiro_numero = input("digite o primeiro_numero: ")
operacao = input("digite  a operacao desejada: + - * / ")
segundo_numero = input("digite o segundo_numero: ")


match operacao:
    case " + ":
        primeiro_numero + segundo_numero
    case " - ":
        primeiro_numero - segundo_numero
    case " * ":
        primeiro_numero * segundo_numero
    case " / ":
        primeiro_numero / segundo_numero
    case _:
        print("opcao invalida")

print(f"resultado: {resultado}")
        

print("fim")
