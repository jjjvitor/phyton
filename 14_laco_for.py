import streamlit as st


st.title("laco de repeticao: for")

st.header("exercicio verificando pares e impares")
st.write("digite um algoritimo que soicite ao usuario 5 valores inteiros e ao final mostre: a- quantos numeros sao pares b- quantosnumeros sao impares")

pares = 0
impares = 0



for i in range(1,6):
    numero = st.number_input(f"digite o {i}º numero: ", step=1)
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

if st.button("verificar"):
    st.info(f"quantidade de pares: {pares}")
    st.info(f"quantidade de impares: {impares}")
