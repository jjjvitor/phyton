import os
os.system("cls")

# Criando um vetor (lista).
lista_notas = []

# Constante
QUANTIDADE_NOTAS = 3

# Inserindo notas.
for i in range(QUANTIDADE_NOTAS):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

media = sum(lista_notas) / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

# Mostrar notas:
print("\nResultado:")
for i in range(QUANTIDADE_NOTAS):
    print(f"Nota: {lista_notas[i]}")

print(f"\nMédia: {media}")
print(f"Resultado: {resultado}")