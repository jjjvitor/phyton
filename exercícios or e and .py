import os
os.system("cls")

login_salvo = "maria"
senha_salva = "123"

login = input("digite seu login: ")
senha = input("digite suua senha: ")


if login == login_salvo and senha == senha_salva:
    print("bem-vindo! ")

else:
    print("login ou senha inválidos")
