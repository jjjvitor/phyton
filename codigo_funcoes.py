import os
os.system("cls")


# criando uma funcao
#funcao com passagen de parametros

def saudacao(nome, idade):
    print(f"ola, {nome}! bem-vindo(a)!")
    print(f"sua idade é {idade} anos.")

print("solicitando dados.")
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))


# chamando a funcao.
saudacao(nome, idade)
