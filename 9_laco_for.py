import streamlit as st
import time

st.title("atividade: 1 ")

st.header("laco de repeticao: for")

st.button("iniciar")
for i in range(100,121, 2):
    st.info(i)
    time.sleep(2)