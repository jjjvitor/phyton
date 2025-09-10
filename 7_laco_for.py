import streamlit as st
import time

st.title("laco de repeticao - for")

st.header("contagem.")

numero = st.number_input("digite ate onde quer o laco de repeticao: ",step=1)

if st.button("iniciar"):
    for i in range(1,numero+1):
        st.info(i)
        time.sleep(1)
    st.header("fim")
