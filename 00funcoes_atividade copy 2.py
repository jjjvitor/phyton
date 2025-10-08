import os
import time

os.system("cls")

# funcao sem parametros e sem retorno
def limpa_tela():
    time.sleep(3) # espera 3 segundos.
    os.system("cls")



# funcao com parametros e com retorno.
def somar(n1, n2):
    return n1 + n2

# funcao com parametros e sem retorno.
def mostrar_resultado(soma):
    print(f"resultado: {soma}")



# codigo principal
# funcao sem parametros e sem retorno
limpa_tela() # chamando funcao

primeiro_numero = int(input("digite um numero: "))
segundo_numero = int(input("digite um numero: "))

# funcao com parametros e com retorno.
soma = somar(primeiro_numero, segundo_numero)


# funcao com parametros e sem retorno.
mostrar_resultado(soma)