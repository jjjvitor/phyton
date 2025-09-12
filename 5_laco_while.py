import os
os.system("cls")

print("laco de repeticao - while")
print("escreva um algoritimo que solicite duas notas para um aluno, caso seja menor que 0 ou maior que 10, mostre a pergunta novamente, calcule e mostre a media aritmetica do aluno")

quantidade_notas = 2
soma = 0

for i in range(quantidade_notas):
    while True:
        nota = int(input(f"digite a {i+1}ª nota: "))
        if nota >= 0 and nota <= 10:
            break
    soma = soma + nota
media = soma / quantidade_notas

print(f"media: {media}")


