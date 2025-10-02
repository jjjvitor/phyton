import os
os.system("cls")

# criando um vetor
lista_numeros = []

#definindo quantidade de numeros
quantidade_numeros = 5

print(f"solicitando {quantidade_numeros} numeros.")
for i in range(quantidade_numeros):
    numero = float(input(f"digite o {i+1}º numero: "))
    # inserindo um numero na lista de numeros
    lista_numeros.append(numero)

# verificando maior e menor numero
menor = min(lista_numeros)
maior = max(lista_numeros)

print("\nmostrando todos os numeros.")
for i in range(5):
    # o valor da variavel i comeca com zero.
    # o valor de i no vetoee faz mostrar o indice no vetor.
    print(f"numero: {lista_numeros[i]}")

print(f"\nmenor numero: {menor}")
print(f"maior nuemro: {maior}")