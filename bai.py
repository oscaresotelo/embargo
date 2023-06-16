
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
pregunta = '''
usando streamlit , deberas conectarte a una base de datos sqlite llamada "embargos.db", deberas trabajar
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

pregunta = pregunta +  "  mostrar el dni numero 24340099, ES IMPORTANTE QUE SOLO MUESTRES EL CODIGO GENERADO SIN COMENTARIOS NI EXPLICACION, y la base de datos es embargos.db"
corregir = """corregir el siguiente codigo, no cambiar la idea principal del codigo,  verificar que la sintaxis sea la correcta y las librerias esten importadas correctamente 
y si las librerias estan actualizadas, tambien controlar que las funciones declaradas cumplan con la sintaxis correspondiente, y si las
librerias estan declaras correctamente y los controles widgtes cumplen con la sintaxis de streamlit, 
el codigo es el siguiente:   
"""
respuesta = generate_story(pregunta)
print(respuesta)
corregir = corregir + respuesta
final = generate_story(corregir)
print(final)
# print(extract_python_code(respuesta))
