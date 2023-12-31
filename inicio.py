        
import streamlit as st
import sqlite3
from st_pages import Page, show_pages, add_page_title
import base64
import pandas as pd 
from datetime import date, timedelta
from notificacion import notif 
import time


# Connect to the SQLite database
conn = sqlite3.connect("embargos.db")
LOGO_IMAGE = "./imagenes/justice.png"

# Create a cursor
c = conn.cursor()

hide_st_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: black !important;
        padding-top: 50px !important;
    }
    .logo-img {
        float:right;
    }
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">Juicios-Embargos</p>
    </div>
    """,
    unsafe_allow_html=True
)

if "ingreso" not in st.session_state:
    st.session_state.ingreso = ""

def login():
    st.session_state.ingreso = "ok"
    st.success("Bienvenido!")
    st.write(notif())
    with open("manualdeusuario.docx", "rb") as file:
        encoded_file = base64.b64encode(file.read()).decode()
        st.markdown(
            f'<a href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{encoded_file}" download="manualdeusuario.docx">Descargar Manual de Usuario</a>',
            unsafe_allow_html=True
        )
    show_pages([
        Page("inicio.py", "Inicio", ":notebook:"),
        Page("carga.py", "Carga", ":notebook:"),
        Page("tipomedidas.py", "Tipos de Medidas", ":notebook:"),
        Page("tiporadicaciones.py", "Tipos de Radicaciones", ":notebook:"),
        Page("reportedni.py", "Consulta por Dni", ":notebook:"),
        Page("reportes.py", "Consulta Fecha Inicio", ":notebook:"),
        Page("actualizar.py", "Modificar Datos", ":notebook:"),
        Page("consultagral.py", "Consulta General", ":notebook:"),
        Page("codigocivil.py", "Consulta Codigo Civil", ":notebook:"),
    ])

# Create the login form
if st.session_state.ingreso == "ok":
    st.write(notif())
    st.header("Salir del Sistema")

    if st.button("Salir"):
        del st.session_state.ingreso
        st.info("Sesión cerrada exitosamente")
        time.sleep(2)
        st.experimental_rerun()
        
else:
    st.header("Iniciar sesión")
    placeholder = st.empty()
    with placeholder.form("Login"):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        ingresar = st.form_submit_button("Ingresar")

    if ingresar:
        # Check if the username and password are valid
        c.execute("SELECT * FROM usuarios WHERE usuario = ? AND password = ?", (username, password))
        user = c.fetchone()

        # If the username and password are valid, log the user in
        if user is not None:
            login()
            placeholder.empty()
        else:
            st.error("Usuario o contraseña incorrecta")
