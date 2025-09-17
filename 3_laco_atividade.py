import streamlit as st

st.title("laco de repeticao")
st.write("crie um programa que solicite ao usurario seu login e uma senha"\
"o programa deve continuar pedindo o login e a senha ate que ambos estejam corretos")

login_salvo = "marta"
senha_salva = "123"

login = st.text_input("digite seu login: ")
senha = st.text_input("digite sua senha: ", type="password")

if st.button("verificar"): 
    if login == login_salvo and senha == senha_salva:
        st.success("bem vindo")
    else:
        st.warning("login ou senha invalidos.")

        

