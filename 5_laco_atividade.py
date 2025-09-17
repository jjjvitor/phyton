import streamlit as st

st.title("laco de repeticao")
st.write("crie um programa que solicite ao usurario seu login e uma senha"\
"o programa deve continuar pedindo o login e a senha ate que ambos estejam corretos")

login_salvo = "marta"
senha_salva = "123"

st.session_state.setdefault("desabilitar", False)
st.session_state.setdefault("tentativas", 0)


login = st.text_input("digite seu login: ", disabled=st.session_state.desabilitar)
senha = st.text_input("digite sua senha: ", type="password", disabled=st.session_state.desabilitar)


if st.button("verificar"): 
    if login == login_salvo and senha == senha_salva:
        st.success("bem vindo")
    else:
        st.session_state.tentativas += 1
        if st.session_state.tentativas <= 3:
            st.warning("login ou senha invalidos, tentativas: {st.session_state.tentativas}")
        else:
            st.session_state.desabilitar = True
            st.error("numero de tentativas invalidas")
    