import os
os.system("cls")

quantidade_numeros = 6
lista_numeros = []
pares = 0
impares = 0


print(f"solicitando {quantidade_numeros} numeros")
for i in range(quantidade_numeros):
    numero = float(input("digite um numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    lista_numeros.append(numero)
      
        
print(f"\nmostrando todos os numeros.")
for i in range(quantidade_numeros):
    print(f"numero: {lista_numeros[i]}")
    
print(f"\nquantidade de pares: {pares}")
print(f"quantidade de impares: {impares}")
