import os 
os.system("cls")


preco_total = 0

while True:
    print("""
=====menu=====
codigo\t     prato\t    \tvalor
1            picanha        25.00
2            lasanha        20.00  
3            strogonoff     18.00
4            bife acebolado 15.00
5            pao com ovo    5.00
""")
    
    opcao = int(input("digite o codigo da opcao desejada: "))

    match opcao:
        case 1:
            prato = "picanha"
            valor = "25"
        case 2:
            prato = "lasanha"
            valor = "20"
        case 3:
            prato = "strogonoff"
            valor = "18"
        case 4:
            prato = "bife acebolado"
            valor = "15"
        case 5:
            prato = "pao com ovo"
            valor = "5"
        case _:
            print("opcao invalida")
            print("tente novamente")
            preco = 0

    preco_total = preco_total + preco_total

    mais_pedidos = input("deseja fazer outro pedido? \nuse s ou n para responder:  ").upper()

    if mais_pedidos == "N":
        break
    os.system("cls")

print("\n ===restaurante===")
print(f"prato escolhido: {prato}")
print(f"valor do prato: {valor}")
print(f"total a pagar: {preco_total}")