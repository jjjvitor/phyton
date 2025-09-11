import streamlit as st
import time

st.title("atividade: 4")

st.header("laco de repeticao: for")
st.write("escrever um algoritimo que solicite ao usuario um numero e faca a contagem regressiva a partir do numero informado ate o numero 1, aguardando um segundo para exibir cada numero")

numero = st.number_input("digite um numero: ", step=1, min_value=0)

if st.button("iniciar"):
    for i in range(numero, 0, -1):
        st.warning (i)
        time.sleep(1)
    st.header("fim")
else:
    st.info("informe um numero")


