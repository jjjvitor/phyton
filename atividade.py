
import streamlit as st
import time

st.title("atividade: 2")

st.header("laco de repeticao: for")

st.write("escrever um algoritimo que mostra os numeros impares entre 1 e 20.")
st.write("clique no botao para iniciar.")




if st.button("iniciar"):
    for i in range(1,21, 2):
        st.info(i)
        time.sleep(1)
st.header("fim")


-------------------------

import streamlit as st
import time

st.title("verificando")

st.header("laco de repeticao: for")
st.write("escrever um algoritimo de computador que solicite so usuario 3 notas e, ao final aresente a media e mostre para o usuario se o aluno esta aprovado, em recuperacao ou reprovado. considere que para aprovaçao, deve-se obter media maior ou igual a 7 para ser reprovado a media deve ser menor que 4")

quantidade_notas = 3
soma = 0

for i in range(quantidade_notas):
    nota = st.number_input(f"digite a {i+1}ª nota: ")
    soma = soma + nota

media = soma / quantidade_notas

if st.button("mostrar resultado"):
    st.info(f"media: {media:.1f}")
    if media >= 7:
        st.success(f"aprovado")
    elif media >= 4:
        st.warning(f"recuperacao")
    else:
        st.error(f"reprovado")

        ------------------------------------







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

--------------





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






import os
os.system("cls")

quantidade_notas = 2
soma = 0

for i in range(quantidade_notas):
    while True:
        nota = float(input("digite uma nota: "))
        if nota < 0 or nota > 10:
            print("a nota invalida")
        else:
            soma += nota
            break

media = soma / quantidade_notas

print(f"media: {media}")