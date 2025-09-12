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
