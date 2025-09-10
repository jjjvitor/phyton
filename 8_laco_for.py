import streamlit as st
import time

st.title("laco de repeticao - for")

st.header("contagem.")

numero = st.write("100 - 120")

if st.button("iniciar"):
    for i in range(100,numero+2):
        st.info(i)
        time.sleep(1)
    st.header("fim")