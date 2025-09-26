import os
os.system("cls")

soma = 0
quantidade_notas = 0

while True:
    nota = float(input("digite a nota: "))
    # quantidade_notas = quantidade_notas  + 1
    # soma = soma +nota
    quantidade_notas += 1
    soma +=1

    resposta = input("deseja adicionar outra nota \n use s ou n para responder."). lower()
    if resposta == "n":
        print("calculando media...")
        break

media = soma / quantidade_notas

print(f"\nmedia: {media}")
print(f"quantidade de loops: {quantidade_notas}")