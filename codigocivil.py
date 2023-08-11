
from bardapi import Bard
import os
import requests
import streamlit as st 
import base64
import re 
from duckduckgo_search import DDGS
from contexto import explicacion

os.environ['_BARD_API_KEY'] = "ZwhlcpEl1aCU7ftwDxiilDY9YU3-1n6xAagHdotas_ZjWW5r70vhRGzE7GidCtkMrMZtDQ."


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



def extraer_numeros(texto):
    """Función para extraer los números de un texto usando expresiones regulares."""
    return re.findall(r'\d+', texto)


def buscar_articulo(articulo_numero):
    with open('codigocivilycomercial.txt', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for i, linea in enumerate(lineas):
            if linea.startswith(f'ARTICULO {articulo_numero}'):
                resultado = linea
                j = i + 1
                while j < len(lineas) and not lineas[j].startswith('ARTICULO'):
                    resultado += lineas[j]
                    j += 1
                
                
                return resultado
                
        return None


contexto = """  
Actua como el actual codigo civil y comercial de Argentina, deberas contestar todas la preguntas en base a los articulos contenidos
del codigo civil y comercial de argentina, señalando los articulos relacionados a la pregunta,¡SIEMPRE ESCRIBE SOLO TU RESPUESTA PRECISA!, la pregunta es la siguiente: 

"""

texto = st.text_area("Ingresar Pregunta") 
prompt = contexto + texto

if "codart" not in st.session_state:
                st.session_state.codart = ""

if "juris" not in st.session_state:
                st.session_state.juris = ""

boton_procesar = st.button("Procesar Pregunta")
if boton_procesar:
    del st.session_state.juris
    del st.session_state.codart
    with st.spinner('Procesando Solicitud...'):
        
        respuesta = bard.get_answer(prompt)['content']
        # st.write(respuesta)
        expander = st.expander("Ver Respuesta")
        expander.write(respuesta)

        numeros_encontrados = extraer_numeros(respuesta)
        if numeros_encontrados:
            st.header("Articulos Mencionados en La Respuesta")
            
            for num in numeros_encontrados:
                if "codart" not in st.session_state:
                    st.session_state.codart = ""
                articulo_encontrado = buscar_articulo(num)
                

                if articulo_encontrado:
                    
                    st.session_state.codart = articulo_encontrado  + st.session_state.codart
                    # st.write( st.session_state.codart)
                    # varrespuestafinal = st.expander("Ver Articulos Mencionados en La Respuesta")
                    # varrespuestafinal.write(st.session_state.codart)
                else:
                    st.write(f'El artículo {num} no fue encontrado en el archivo.')
        else:
            st.write("No se encontraron números en la respuesta.")
        varrespuestafinal = st.expander("Ver Articulos Mencionados en La Respuesta")
        varrespuestafinal.write(st.session_state.codart)
        st.header("jurisprudencia Econtrada en la Web")
        with DDGS() as ddgs:
            if "juris" not in st.session_state:
                st.session_state.juris = ""
            busquedaweb = texto + ', jurisprudencia argentina '
            
            for r in ddgs.text(busquedaweb, region='ar-es', safesearch='Off', timelimit='y'):
                st.session_state.juris = str(r) + st.session_state.juris

                verresultados = st.expander("Ver jurisprudencia Encontrada en la Web")
                verresultados.write(r)
    # explicacionarticulo = st.session_state.codart + "explicar estos articulos del codigo civil y comercial argentino"
    # explicacionarticulo = st.session_state.codart 
    
    # final = explicacion(explicacionarticulo, contexto)
    # st.write(final)
    # respuestafinal = bard.get_answer(final)['content']

    # varrespuestafinal = st.expander("Ver Articulos Mencionados en La Respuesta")
    # varrespuestafinal.write(st.session_state.codart)
    # verresultados = st.expander("Ver jurisprudencia Encontrada en la Web")
    # verresultados.write(st.session_state.juris)
# numero_articulo = st.number_input('Ingrese el número de artículo:', min_value=0, value=0, step=1)
# articulo_encontrado = buscar_articulo(numero_articulo)

# if articulo_encontrado:
#     st.write(articulo_encontrado)
# else:
#     st.write('El artículo especificado no fue encontrado en el archivo.')