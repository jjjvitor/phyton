import os
os.system("cls")


print("""

codigo      mes
1           janeiro
2           feveiro
3           marco
4           abril
5           maio
6           junho
7           julho
8           agosto
9           setembro
10          outubro
11          novembro
12          dezembro

""")

codigo = int(input("digite o codigo do mes desejado: "))

match codigo:
    case 1:
        mes = "janeiro"
    case 2:
        mes = "fevereiro"
    case 3:
        mes = "marco"
    case 4:
        mes = "abril"
    case 5:
        mes = "maio"
    case 6:
        mes = "junho"
    case 7:
        mes = "julho"
    case 8:
        mes = "agosto"
    case 9:
        mes = "setembro"
    case 10:
        mes = "outubro"
    case 11:
        mes = "novembro"
    case 12:
        mes = "dezembro"
    case _:
        print("opcao invalida")

print(f"mes: {mes}")
    
    
