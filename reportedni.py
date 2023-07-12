import streamlit as st
import pandas as pd
import sqlite3
from fpdf import FPDF
import base64

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
        <h1 style='text-align: center;'>Juicios-Embargos</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Función para generar el informe en PDF y obtener el contenido del archivo
def generate_pdf_report(data):
    pdf = FPDF()
    pdf.add_page()

    # Agrega el encabezado
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Informe de embargos por Fecha de Inicio", ln=True, align="C")

    # Agrega los datos de la consulta
    pdf.set_font("Arial", "", 10)
    for _, juicio in data.iterrows():
        for col, value in juicio.items():
            pdf.cell(0, 10, f"{col}: {value}", ln=True)

    # Obtén el contenido del PDF
    output = pdf.output(dest="S").encode("latin-1")

    return output

# Conexión a la base de datos
conn = sqlite3.connect("embargos.db")

# Consulta por DNI
# @st.cache_data(persist=True)
def get_juicios(dni):
    query = f"SELECT * FROM Juicios WHERE dni = '{dni}'"

    return pd.read_sql_query(query, conn)

# Interfaz de usuario con Streamlit
def main():
    st.markdown("<h1 style='text-align: center;'>CONSULTAS</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Embargos por DNI</h1>", unsafe_allow_html=True)

    # Campo DNI
    dni = st.text_input("Ingrese el DNI")

    # Consulta y generación del informe
    if st.button("Generar informe"):
        juicios = get_juicios(dni)
        if juicios.empty:
            st.info("No se encontraron registros para ese DNI.")
        else:
            st.info(f"Se encontraron {len(juicios)} registros para ese DNI.")
            pdf_output = generate_pdf_report(juicios)
            st.dataframe(juicios)
            st.markdown(get_download_link(pdf_output), unsafe_allow_html=True)

# Función para generar el enlace de descarga
def get_download_link(file_content):
    b64 = base64.b64encode(file_content).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="reporte_embargos.pdf">Descargar informe PDF</a>'
    return href

if __name__ == "__main__":
    main()
