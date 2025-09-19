import os
os.system("cls")

soma = 0
pares = 0
impares = 0
quantidade_numeros = 0
quantidade_pares = 0
quantidade_impares = 0

while True:
    numero = int(input("digite um numero: "))
    if numero == 0:
        break
    quantidade_numeros += 1
    soma += numero

    if numero % 2 == 0:
        pares = pares + 1 
    else:
        impares = impares + 1
       

media = soma / quantidade_numeros


print(f"quantidade_pares: {quantidade_pares}")
print(f"\nmedia: {pares}") 
print(f"quantidade_impares: {quantidade_impares}")
print(f"\nmedia: {media}")
        
        
