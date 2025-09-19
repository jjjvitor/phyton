import os 
os.system("cls")

soma = 0
quantidade_notas = 0

while True:
    nota = float(input("digite uma nota: "))
    # quantidade_notas = quantidade_notas  + 1
    # soma = soma +nota
    quantidade_notas += 1
    soma += nota
    resposta = input("deseja adicionar mais uma nota \nuse s ou n para responder: ").lower()
    if resposta == "n":
        break

media = soma / quantidade_notas
        
        
print(f"\nmedia: {media}")
print(f"quantidade_loops: {quantidade_notas}")
