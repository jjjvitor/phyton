import os 
os.system("cls")



numeros = []
soma_positivos = 0
quantidade_negativos = 0


for i in range(5):
    numero = float(input("digite um numero: "))
    numeros.append(numero)
    
    if numero > 0:
        soma_positivos += numero
    elif numero < 0:
        quantidade_negativos += 1

print("\n= resultado =")

for numero in numeros:
    print(f"numero: {numero}")

print(f"soma de numeros positivos: {soma_positivos}")
print(f"quantidade de numeros negativos: {quantidade_negativos}")