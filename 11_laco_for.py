import streamlit as st
import time
st.title("atividade: 3")

st.header("laco de repeticao: for")

st.write("escreva um algoritimo que solicite do usuario um numero e mostre a tabuada de multiplicacao do numero informado")
st.write("clique no botao para iniciar")

numero = st.number_input("digite um numero: ", step=2)



if st.button("iniciar"):
    for i in range(1,11):
          st.info(f"{numero} x {i} = {numero * 1}")
          st.write(i)
          time.sleep(1)
st.header("fim")