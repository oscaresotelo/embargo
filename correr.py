import streamlit as st
import ast

def run_streamlit_code(code):
    # Ejecuta el código escrito en el control text_area
    try:
        # Utiliza el AST para compilar y ejecutar el código
        compiled_code = compile(ast.parse(code), filename='<string>', mode='exec')
        exec(compiled_code)
    except Exception as e:
        st.error(f"Error de ejecución: {e}")

def main():
    st.title("Ejecutar Código de Streamlit")
    
    # Control text_area para escribir código de Streamlit
    code = st.text_area("Escribe tu código de Streamlit aquí")
    
    # Botón para ejecutar el código
    if st.button("Ejecutar"):
        exec(code, globals())

if __name__ == "__main__":
    main()

