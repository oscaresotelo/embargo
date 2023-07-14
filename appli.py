import streamlit as st  

st.title("prueba")

if "nombre" not in st.session_state:
	st.session_state.nombre = ""
st.write(st.session_state.nombre)
var = st.text_input("ingres nombre")
st.session_state.nombre = var

if st.button("guardar"):
	st.write(st.session_state.nombre)