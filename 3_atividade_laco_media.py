import os
os.system("cls")

quantidades_numeros = 0
soma = 0

while True:
    numero = int(input("digite um numero: "))
    # quantidade_notas = quantidade_notas  + 1
    # soma = soma +nota
    if numero < 0:
        break
    quantidades_numeros += 1
    soma += numero

media = soma / quantidades_numeros

print(f"\nmedia: {media}")
