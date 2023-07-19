
from bardapi import Bard
import os
import requests
import streamlit as st 
import base64
os.environ['_BARD_API_KEY'] = "YwhlcoKaK4On2dndWfbCoX9MifhxeC_5mVs6d6WAHBlGs3J88otYTjI0NKeHYH4R90VSrQ."

LOGO_IMAGE = "./imagenes/justice.png"

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
st.markdown(hide_st_style, 

    unsafe_allow_html=True)
st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">CONSULTA-CODIGO CIVIL</p>
    </div>
    """,
    unsafe_allow_html=True
)
session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))


bard = Bard(timeout=30, session=session)  # Set timeout in seconds



contexto = ", segun el nuevo CODIGO CIVIL Y COMERCIAL DE LA NACION ARGENTINA QUE ENTRO EN VIGENCIA EN EL  año 2015, Ley 26.994, y mostrar textualmente el articulo y numero de articulo  "



prompt = st.text_area("Ingresar Pregunta") + contexto



boton_procesar = st.button("Procesar Pregunta")
with st.spinner('Procesando Solicitud...'):
    if boton_procesar:
    	respuesta = bard.get_answer(prompt)['content']
        # st.write(respuesta)
    	st.write(respuesta)