import streamlit as st

st.title("logica de progamacao")

st.header("laco de repeticao - while")


while True:
    numero = st.number_input("digite um numero: ", step=1)
    if numero == 2:
        break

st.header("fim")