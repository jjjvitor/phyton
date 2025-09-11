import streamlit as st
import time

st.title("atividade 5")

st.header("laco de repeticao: for")
st.write("escrever um programa de computador que solicite ao usuario 5 numeros inteiros e, ao final, apresente a soma de todos os numeros lidos")

soma = 0

for i in range(1,6):
    numero = st.number_input(f"digite o {i}º numero: ", step=1, min_value=0)
    soma = soma + numero
    time.sleep(1)
    
if st.button("iniciar"):
    st.success(f"a soma dos numeros e: {soma}")
else:
    st.info("informe um numero")

