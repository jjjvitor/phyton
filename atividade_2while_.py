import os
os.system("cls")

#definindo valor inicial para contadores
pares = 0
impares = 0
soma_pares = 0
soma_geral = 0
contador_geral = 0

while True:
    numero = int(input("digite um numero: "))
    if numero > 0:
        contador_geral += 1
        soma_geral += numero

        if numero % 2 == 0:
            pares += 1
            soma_pares += numero
        else:
            impares += 1
    if numero == 0:
        break
    
#calculando
#operacao ternaria

### media_pares = soma_pares / pares if pares != 0 else 0
### media_geral = soma_geral / contador_geral if contador_geral != 0 else 0
if pares != 0:
    media_pares = soma_pares / pares
else:
    media_pares = 0

if contador_geral != 0:
    media_geral = soma_geral / contador_geral
else:
    media_geral = 0
 
#exibindo resultados>
print(f"\nquantidade de pares: {pares}")
print(f"quantidade de impares: {impares}")
print(f"media de numeros pares: {media_pares}")
print(f"media geral: {media_geral}")

    



