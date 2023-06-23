import streamlit as st
from baichat_py import Completion
import re

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

def generate_story(prompt):
    story = ""
    for token in Completion.create(prompt):
        story += token
    return story

def main():
    st.title("Embargos App")
    
    pregunta = '''
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
        ES IMPORTANTE QUE GENERES EL CODIGO SE GENERE EN UN SOLO ARCHIVO,  NO COMENTAR EL CODIGO NI EXPLICAR LO QUE HICISTE, el pedido es el siguiente:
    '''
    corregir = """corregir el siguiente codigo, IMPORTANTE RECORDAR QUE SE ESTA TRABAJANDO CON EL FRAMEWORK STREAMLIT:
    """


    mostrar_dni = st.text_area("ESCRIBE TU CONSULTA")

    if st.button("Ejecutar"):
        pregunta = pregunta + mostrar_dni
        
        respuesta = generate_story(pregunta)
        st.write(respuesta)
        codigo_corregido = extract_python_code(respuesta)
        # st.write(codigo_corregido)
        # corregir = corregir + respuesta
        # st.write(codigo_corregido)
        # final = generate_story(corregir)
        # st.write(final)
        exec(codigo_corregido, globals())

if __name__ == "__main__":
    main()
