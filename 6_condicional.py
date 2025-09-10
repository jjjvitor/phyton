import streamlit as st

st.title("verificando numeros")


primeiro_numero = st.number_input("digite o primeiro numero: ")
segundo_numero = st.number_input("digite o segundo numero: ")




soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = (primeiro_numero + segundo_numero) /2
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)
 
 
if st.button("verificar"):
    st.write(f"soma: {soma}")
    st.write(f"produto: {produto}")
    st.write(f"media: {media}")
    st.write(f"maior: {maior}")
    st.write(f"menor: {menor}")
else:
    st.info("informe os numeros.")
