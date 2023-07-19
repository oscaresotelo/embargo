import asyncio
import os
from sydney import SydneyClient
import pandas as pd 
import streamlit as st  
import re 
import base64

os.environ["BING_U_COOKIE"] = "<your-cookie>"

async def main(pregunta) -> None:
    async with SydneyClient() as sydney:
        response = await sydney.ask(pregunta)
        return(response)
contexto = ", buscar en el contexto del codigo civil y comercial argentino y mostrar el o los articulos referentes  "
st.title("CONSULTA AL CODIGO CIVIL Y COMERCIAL")


prompt = st.text_area("Ingresar Pregunta") + contexto



boton_procesar = st.button("Procesar Pregunta")

if boton_procesar:
	respuesta = asyncio.run(main(prompt))
    # st.write(respuesta)
	st.write(respuesta)