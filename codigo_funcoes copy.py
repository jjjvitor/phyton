import os
os.system("cls")


#funcao com passagen de parametros
# criando uma funcao
def saudacao(nome, idade, altura, peso, nacionalidade):

    print(f"ola, {nome}! bem-vindo(a)!")
    print(f"sua idade é {idade} anos.")
    print(f"sua altura é {altura}.")
    print(f"seu peso é {peso}.")
    print(f"sua nacionalidade é {nacionalidade}")

print("solicitando dados.")
 
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura:"))
peso = float(input("digite seu peso: "))
nacionalidade = input("digite sua nacionalidade: ")

# chamando a funcao.
saudacao(nome, idade, altura, peso, nacionalidade)
