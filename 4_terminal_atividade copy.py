import os
os.system("cls")

print("")


login_salvo = "marta"
senha_salva = "123"


while True:
    for i in range(3):   
        print(f"tentativa: {i+1}")
        login = input("digite seu login: ")
        senha = input("digite sua senha: ")

        if login == login_salvo and senha_salva:
            print("bem vindo")
            break
        else:
            print("login ou senha invalidos.\n")
    break
            
            
            
        
            
            
        