import os
os.system("cls")

def calcular_media(n1, n2):
    calcular = (n1 + n2) / 2
    return calcular

# funcao com parametros e sem retorno.
def mostrar_resultado(media):
    print(f"resultado: {media}")
    if media >= 7:
        print("aprovado")
    else:
        print("reprovado")



# codigo principal
# funcao sem parametros e sem retorno 

primeiro_numero = int(input("digite um numero: "))
segundo_numero = int(input("digite um numero: "))

# funcao com parametros e com retorno.
media = calcular_media(primeiro_numero, segundo_numero)


# funcao com parametros e sem retorno.
mostrar_resultado(media)
    
    

