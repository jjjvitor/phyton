import os
os.system("cls")

print("")

tentativas = 0
tentativas = 0
login_salvo = "marta"
senha_salva = "123"

for i in range(3):
    while True:
        if tentativas >= 3:
            break
        print(f"tentativa: {tentativas}")
        login = input("digite seu login: ")
        senha = input("digite sua senha: ")

        if login == login_salvo and senha_salva:
            print("bem vindo")
            break
        else:
            print("login ou senha invalidos")
            tentativas += 1
            
            
        
            
            
        