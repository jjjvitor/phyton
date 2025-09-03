import os
os.system("cls")

print("""
codigo   prato           valor
      
 1       picanha         r$ 25,00
 2       lasanha         r$ 20,00
 3       strogonoff      r$ 18,00
 4       bife acebolado  r$ 15,00
 5       pao com ovo     r$ 5,00
      
""")

codigo = int(input("digite o codigo do prato desejado: "))

match codigo:
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
        print("opcao invalida")

print (f"prato: {prato}")
print (f"preco: {preco}")
    
        












































