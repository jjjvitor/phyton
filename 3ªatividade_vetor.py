import os 
os.system("cls")

lista_pratos = []
precos_pratos = []

while True:
    opcao = int(input("""
codigo\t     prato\t    \tvalor
    1        picanha       r$ 25.00
    2        lasanha       r$ 20.00  
    3        strogonoff    r$ 18.00
    4        bife acebolado r$ 15.00
    5        pao com ovo   r$ 5.00
                      
digite a opcao desejada: """))
    
    match opcao:
        case 1:
            prato = "picanha"
            preco = 25
        case 2:
            prato = "lasanha"
            preco = 20
        case 3:
            prato = "strogonoff"
            preco = 18
        case 4:
            prato = "bife acebolado"
            preco = 15
        case 5:
            prato = "pao com ovo"
            preco = 5
        case _:
            print("opcao invalida. \ntente novamente.\n")
            preco = 0

    if opcao >= 1 and opcao <= 5:
        lista_pratos.append(prato)
        precos_pratos.append(preco)
   

    continuar = input("deseja fazer outro pedido? \nresponda com s ou n").lower()
    if continuar == "n":
        break
    os.system("cls")

if sum(precos_pratos) == 0:
    print("\nnenhum prato foi escolhido")
else:
    print("\n= pratos escolhidos=")
    for prato in lista_pratos:
        print(f"prato: {prato}")

    print(f"\ntotal: r$ {sum(precos_pratos):.2f}")
print("\nvolte sempre!")




