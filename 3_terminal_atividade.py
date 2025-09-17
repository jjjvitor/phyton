import os
os.system("cls")

print("crie um programa que solicite ao usuario seu login e uma senha"\
"o programa deve continuar pedindo o login e a senha ate que ambos estejam corretos")

login_salvo = "marta"
senha_salva = "123"

while True:
    login = input("digite seu login: ")
    senha = input("digite sua senha: ")

    if login == login_salvo and senha_salva:
        print("bem vindo")
        break
    else:
        print("login ou senha invalidos")