import os
os.system("cls")

print("crie um algoritimo que receba do usuario valores e armazene em um vetor 5 numeros, caso seja informado um valor negativo, atribua o valor 0. liste os valores do vetor")

lista_numeros = []


print("solicitando numeros")
for i in range(5):
    numero = int(input(f"digite o {i+1}º numero: "))
    if numero < 0:
        numero = 0
    lista_numeros.append(numero)
    
print(f"\n exibindo numeros.")
for i, numero in enumerate (lista_numeros, start = 1):
    print(f"{i}º numero: {numero}")


    