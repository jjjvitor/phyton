import os
os.system("cls")

nota1 = input("digite a primeira  nota: ")
nota2 = input("digite a segunda  nota: ")
nota3 = input("digite a terceira  nota: ")

media = (nota1 + nota2 + nota3) / 3
media = 0

if media >= 7:
    print("aprovado")
elif media >= 5 or media <= 6.9:
    print("recuperacao")
else:
    print("reprovado")

print("fim")