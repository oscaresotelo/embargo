import streamlit as st
import pandas as pd
import sqlite3
from fpdf import FPDF
import base64
st.markdown(
    """
    <style>
        div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
        /* Estilos generales */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f1f1f1;
            margin: 0;
            padding: 0;
        }
        button.step-up {display: none;}
        button.step-down {display: none;}
        div[data-baseweb] {border-radius: 4px;}
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            border-radius: 4px;
        }
        
        h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        
        /* Estilos del formulario */
        form {
            margin-bottom: 20px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        .form-group input[type="text"],
        .form-group input[type="number"],
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        
        .form-group textarea {
            height: 100px;
            resize: vertical;
        }
        
        .form-submit-button {
            display: block;
            width: 100%;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        
        .form-submit-button:hover {
            background-color: #0056b3;
        }
        
        .success-message {
            margin-top: 20px;
            padding: 10px;
            color: #155724;
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 4px;
        }
        
        .error-message {
            margin-top: 20px;
            padding: 10px;
            color: #721c24;
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            border-radius: 4px;
        }
    </style>
    """,
    unsafe_allow_html=True,
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

# Consulta de registros entre dos fechas

def get_juicios(start_date, end_date):
    query = f"SELECT * FROM Juicios WHERE FechaInicio BETWEEN '{start_date}' AND '{end_date}'"
    return pd.read_sql_query(query, conn)

# Interfaz de usuario con Streamlit
def main():

    st.markdown("<h1 style='text-align: center;'>CONSULTAS</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Embargos por Fecha de Inicio</h1>", unsafe_allow_html=True)
    

    # Rango de fechas
    start_date = st.date_input("Fecha de inicio")
    end_date = st.date_input("Fecha de fin")

    if start_date > end_date:
        st.error("La fecha de inicio debe ser anterior a la fecha de fin.")
        return

    # Consulta y generación del informe
    if st.button("Generar informe"):
        juicios = get_juicios(start_date, end_date)
        if juicios.empty:
            st.info("No se encontraron registros en ese rango de fechas.")
        else:
            st.info(f"Se encontraron {len(juicios)} registros en ese rango de fechas.")
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
