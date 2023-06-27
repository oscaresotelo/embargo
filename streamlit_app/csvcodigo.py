

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
    # pedido = """crear aplicacion en streamlit, verificar que las bibliotecas esten actualizadas de pandas y las que sean necesarias
    # recordar que .append no es compatible con pandas o dataframes , comprobar la sintaxis del codigo antes de 
    # mostrar el resultado final , IMPORTANTE todo el codigo debe estar en un solo archivo.
    #  El pedido es el siguiente:
    # """
    pedido = '''
    import streamlit as st, estas trabajando con streamit y Estas trabajando con pandas dataframe en python.El nombre del dataframe es "df",
    IMPORTANTE AL IMPORTAR UN ARCHIVO CVS DEBES OBTENER EL NOMBRE DE LAS COLUMNAS Y TRABAJAR EN RELACION A ESTOS NOMBRES, 
    IMPORTANTE USAR streamlit, IMPORTANTE GENENERAR TODO EL CODIGO EN UN SOLO ARCHIVO, USAR CONTROLES respetando EL TIPO DE DATO DE LA COLUMNA
    DEL ARCHIVO, por ejemplo si es flot64 usan st.number_input, la solicitud es lo siguiente:
    '''
    prompt = st.text_area(" ")
    pregunta = pedido + prompt

    if st.button("Enviar"):
        resp = gpt3.Completion.create(prompt= pregunta)
        # st.write(resp)
        generated_text = resp.get("text", "")

        st.session_state.codigo = extract_python_code(resp.get("text", ""))
        # st.text_area("", extract_python_code(resp.get("text", "")), disabled=False)

    codigo = st.text_area("", st.session_state.codigo)
    st.session_state.codigo = codigo
    exec(st.session_state.codigo, globals())
    # if st.button("Ejecutar"):
    #     if st.session_state.codigo:
    #         # st.write(st.session_state.codigo)
    #         # Guardar el contenido en un archivo llamado "appli.py"
    #         with open("appli.py", "w",encoding="utf-8") as file:
    #             file.write(st.session_state.codigo)
    #         # Ejecutar el código ingresado utilizando el comando streamlit run
    #         st.write("Ejecutando aplicación...")
    #         cmd = f"streamlit run appli.py"
    #         subprocess.Popen(cmd, shell=True)

if __name__ == "__main__":
    main()


