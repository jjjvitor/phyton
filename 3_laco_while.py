import os 
os.system("cls")

print("laco de repeticao --while")

print("escreva um algoritimo que solicite ao usuario a nota de um aluno, caso seja menor que 0 ou maior que 10, modtre a pergunta novamente. mostre a nota informa pelo usuario")

nota = 0

while True:
    nota = int(input("digite a nota do aluno: "))
    if nota >= 0 and nota <= 10:
        break

        
print(f"nota: {nota}")

    

        


