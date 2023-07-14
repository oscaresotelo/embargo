import sqlite3
import streamlit as st
import pandas as pd
import base64
# Conectarse a la base de datos
conn = sqlite3.connect('embargos.db')
c = conn.cursor()

# Crear tabla Medidas si no existe
c.execute('''CREATE TABLE IF NOT EXISTS Medidas
             (idmedida INTEGER PRIMARY KEY, NombreMedida TEXT)''')
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
        <p class="logo-text">Juicios-Embargos</p>
    </div>
    """,
    unsafe_allow_html=True
)
if "ingreso" not in st.session_state:
      st.session_state.ingreso = ""


if st.session_state.ingreso == "":
    st.warning("Por favor Ingrese Correctamente")
 

else :

# Título de la aplicación
    st.title("Tipo de Medidas")

    # Ingreso de datos
    id_medida = st.number_input("Ingrese el ID de la medida:", value=0, step=1)
    nombre_medida = st.text_input("Ingrese el nombre de la medida:")

    # Botón para guardar los datos
    if st.button("Guardar"):
        # Insertar los datos en la tabla Medidas
        c.execute("INSERT INTO Medidas (idmedidas, NombreMedida) VALUES (?, ?)", (id_medida, nombre_medida))
        conn.commit()
        st.success("Los datos han sido guardados correctamente.")

    # Mostrar los datos existentes en un dataframe
    st.write("Datos existentes en la tabla Medidas:")
    df = pd.read_sql_query("SELECT * from Medidas", conn)
    st.write(df)

    # Cerrar la conexión con la base de datos
    conn.close()
