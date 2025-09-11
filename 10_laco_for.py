#

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