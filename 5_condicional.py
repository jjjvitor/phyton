# verificando a media
# solicite ao usuario a media do aluno
# se amior ou igual a 7, mostre como aprovado
# caso contrario, mostre como reprovado

import streamlit as st

st.title("verificando a media")

media = st.number_input("digite a media: ")


if st.button("verificar"):
    if media >= 7:
        st.success("aprovado.")
    else:
        st.error("reprovado.")

else:
    st.warning("informe media.")

# sucess - verde
# warning - amarelo
# info - azul
# error - vermelho
