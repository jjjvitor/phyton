import os
os.system("cls")

quantidade_notas = 2
soma = 0

for i in range(quantidade_notas):
    while True:
        nota = float(input("digite uma nota: "))
        if nota < 0 or nota > 10:
            print("a nota invalida")
        else:
            soma += nota
            break

media = soma / quantidade_notas

print(f"media: {media}")
