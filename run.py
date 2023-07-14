# from Bard import Chatbot


# # Paste your Bard Token (check README.md for where to find yours) 
# token = "XQhlcrMY8LmPIMgZerlkEworuoOUVxaQYoRksshTR9zaFvt2VDYP1CCf92nPhr60JKKgJg."
# # Initialize Google Bard API
# chatbot = Chatbot(token)

# prompt = """
# import streamlit as st, estas trabajando con streamit y Estas trabajando con pandas dataframe en python.El nombre del dataframe es "df",
#     IMPORTANTE AL IMPORTAR UN ARCHIVO CVS DEBES OBTENER EL NOMBRE DE LAS COLUMNAS Y TRABAJAR EN RELACION A ESTOS NOMBRES, 
#     IMPORTANTE USAR streamlit, IMPORTANTE GENENERAR TODO EL CODIGO EN UN SOLO ARCHIVO, USAR CONTROLES respetando EL TIPO DE DATO DE LA COLUMNA
#     DEL ARCHIVO, por ejemplo si es flot64 usan st.number_input, debes ejecutar el codigo usando python repl , y mostrar el resultado
#     usando print, la solicitud es lo siguiente: mostrar el nombre de las columnas de archivo precios.csv

#  """
# response = (chatbot.ask("hola"))
# print(response['content'])


import asyncio
import os
from sydney import SydneyClient
import pandas as pd 

df = pd.read_csv("maestro.csv")
resultado = df[df["DNI"] == 40695989]
prompt = str(resultado)


    
os.environ["BING_U_COOKIE"] = "<your-cookie>"



# print(pregunta)
# respuesta = asyncio.run(main(pregunta))
# print(respuesta)

pregunta = 'escribir una nota informando al señor javier que es gerente comercial la situacion de los vencimientos de la tarjeta de un cliente, la informacion no debe referirse a deudas: ' + prompt
async def main(pregunta) -> None:
    async with SydneyClient() as sydney:
        response = await sydney.compose(pregunta, format="email")
        print(response)
   

# if __name__ == "__main__":
#     asyncio.run(main())
pregunta = 'necesito que actues como oficinista , escribir una nota informando al gerente comercial la siguiente situacion ' + prompt
asyncio.run(main(pregunta))