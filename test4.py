import asyncio
import os
from sydney import SydneyClient
import pandas as pd 
import streamlit as st  
import re 
import base64
def extract_python_code(text):
    if "```python" in text:
        pattern = r"```python(.*?)```"
    else:
        pattern = r"```(.*?)```"
        
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return ""

if "codigo" not in st.session_state:
        st.session_state.codigo = ""    
os.environ["BING_U_COOKIE"] = "<your-cookie>"


contexto = """ import streamlit as st, import pandas as pd, import base64,Actua como un desarrollador senior de Streamlit,deberas escribir el codigo 
en un solo archivo, la solicitud es la siguiente  : """
st.title("AI-cito")
prompt = contexto + st.text_area("Ingresar Solicitud") 
async def main(pregunta) -> None:
    async with SydneyClient() as sydney:
        response = await sydney.compose(pregunta)
        return(response)
   
boton_procesar = st.button("Procesar")
if boton_procesar:

    respuesta = asyncio.run(main(prompt))
    # st.write(respuesta)
    st.session_state.codigo = extract_python_code(respuesta)
exec(st.session_state.codigo, globals())