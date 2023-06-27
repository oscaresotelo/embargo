

# import streamlit as st
# import re
# from freeGPT import gpt3
# import subprocess



# def extract_python_code(text):
#     if "```python" in text:
#         pattern = r"```python(.*?)```"
#     else:
#         pattern = r"```(.*?)```"
        
#     match = re.search(pattern, text, re.DOTALL)
#     if match:
#         return match.group(1)
#     else:
#         return ""

# def main():
#     if "codigo" not in st.session_state:
#         st.session_state.codigo = ""

#     st.title("CONSULTA DE EMBARGOS-BETA")
#     # pedido = """crear aplicacion en streamlit, verificar que las bibliotecas esten actualizadas de pandas y las que sean necesarias
#     # recordar que .append no es compatible con pandas o dataframes , comprobar la sintaxis del codigo antes de 
#     # mostrar el resultado final , IMPORTANTE todo el codigo debe estar en un solo archivo.
#     #  El pedido es el siguiente:
#     # """
#     pedido = '''
#     import streamlit as st, debes escribir  un documento  respetando el siguiente formato de ejemplo,  reemplazando las palabras segun solicitado
#     , la fecha debe ser la de hoy, el formato es el siguiente:
#                                     San Miguel de Tucuman 20 de Agosto de 2021.-

#          Señor
#          Gerente XXXXXX


#                   AQUI VA EL PEDIDO XXXXXXXXXXXXXXX


#                                      Atentamente.
            

        
#                            Oscar Sotelo
#                            Dni 24.340.099.

#     IMPORTANTE RECORDAR QUE ES UN FORMATO DE EJEMPLO Y  EL TEXTO DEBE CAMBIAR SEGUN EL PEDIDO, REEMPLAZANDO EL CONTENIDO, por lo solicitado
#     USAR ENCODE "utf-8" en el st.write()
#     el pedido es el siguiente:

#     '''
#     prompt = st.text_area(" ")
#     pregunta = pedido + prompt

#     if st.button("Enviar"):
#         resp = gpt3.Completion.create(prompt= pregunta)
#         # st.write(resp)
#         generated_text = resp.get("text", "")
#         st.write(generated_text, encoding = "utf-8")
        

# if __name__ == "__main__":
#     main()

import streamlit as st
import re
from freeGPT import gpt3
import subprocess
import html


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
    soy empleado de la institucion llamada "CAJA POPULAR DE AHORROS", las notas siempre son dirigidas a un superior, 
    debes elaborar   un documento  , IMPORTANTE respetar el siguiente formato de ejemplo,  reemplazando las palabras segun lo solicitado
    , la fecha debe ser la de hoy, el formato es el siguiente:
                                    San Miguel de Tucuman 20 de Agosto de 2021.-

         Señor
         Gerente XXXXXX


                  AQUI VA EL PEDIDO XXXXXXXXXXXXXXX


                                     Atentamente.
            

        
                           

    IMPORTANTE RECORDAR QUE ES UN FORMATO DE EJEMPLO Y  EL TEXTO DEBE CAMBIAR SEGUN LOS DATOS INGRESADOS, REEMPLAZANDO EL CONTENIDO, por lo solicitado
    IMPORTANTE mostrar solo el texto generado,  sin explicacion, reemplazar  Dni 24.340.099 cuando se indique otro dni, mostrar texto generado,
    sin aclaracion, solo mostrar lo generado,
    el pedido es el siguiente:

    '''
    prompt = st.text_area(" ")
    pregunta = pedido + prompt

    if st.button("Enviar"):
        resp = gpt3.Completion.create(prompt=pregunta)
        generated_text = resp.get("text", "")
        generated_text = bytes(generated_text, "utf-8").decode("unicode_escape")
        st.write(generated_text)


if __name__ == "__main__":
    main()
