

import streamlit as st
import re
from freeGPT import gpt3
import subprocess



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

def main():
    if "codigo" not in st.session_state:
        st.session_state.codigo = ""

    st.title("CONSULTA DE EMBARGOS-BETA")
    
    pedido = '''
    usando streamlit , tienes acceso a una base de datos sqlite, deberas conectarte a una base de datos sqlite llamada "embargos.db", deberas trabajar
    con la tabla "Juicios" que tiene los siguientes campos:
    "id"    INTEGER,
        "Dni"   INTEGER,
        "NombreJuicio"  TEXT,
        "NumerodeExpte" INTEGER,
        "RadicacionJudicial"    INTEGER,
        "NumeroOficio"  INTEGER,
        "NumeroExpteAdministrativo" INTEGER,
        "MedidaCautelar"    INTEGER,
        "AclaracionCautelar"    TEXT,
        "FechaInicio"   DATE,
        "FechaFin"  DATE,
        "Observacion"   TEXT,
        "MontoEmbargo"  REAL,
        "Sanciones" INTEGER,
        ES IMPORTANTE QUE GENERES TODO EL CODIGO SE GENERE EN UN SOLO ARCHIVO, TAMBIEN ES IMPORTANTE QUE IMPORTES LA LIBRERIA base64, NO COMENTAR EL CODIGO NI EXPLICAR LO QUE HICISTE, TAMBIEN ES 
        IMPORTANTE QUE TE MANEJES CON EL IDIOMA ESPAÑOL, el pedido es el siguiente:
    '''
    prompt = st.text_area(" ")
    pregunta = pedido + prompt

    if st.button("Enviar"):
        resp = gpt3.Completion.create(prompt= pregunta)
        # st.write(resp)
        generated_text = resp.get("text", "")

        st.session_state.codigo = extract_python_code(resp.get("text", ""))
        # st.text_area("", extract_python_code(resp.get("text", "")), disabled=False)

    # codigo = st.text_area("", st.session_state.codigo)
    # codigo = st.session_state.codigo
    # st.session_state.codigo = codigo
    exec(st.session_state.codigo, globals())
   
if __name__ == "__main__":
    main()


