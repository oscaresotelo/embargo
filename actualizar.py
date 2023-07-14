import streamlit as st
import sqlite3
import pandas as pd
import base64

# Conexión a la base de datos SQLite
conn = sqlite3.connect('embargos.db')
c = conn.cursor()

# Función para buscar registros por DNI
def buscar_por_dni(dni):
    c.execute("SELECT * FROM Juicios WHERE Dni = ?", (dni,))
    return c.fetchall()
def buscar_por_id(id):
    c.execute("SELECT * FROM Juicios WHERE id = ?", (id,))
    return c.fetchall()


# Función para actualizar un registro
def actualizar_registro(id, campo, valor):
    c.execute("UPDATE Juicios SET {} = ? WHERE ID = ?".format(campo), (valor, id))
    conn.commit()
    return c.rowcount

if "id" not in st.session_state:
    st.session_state.id = ""
if "campo" not in st.session_state:
    st.session_state.campo = ""

# Título de la aplicación

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
    st.title("Actualizacion De Registros")
    # Entrada del número de DNI
    dni = st.sidebar.text_input("Ingrese el número de DNI")

    # Botón para buscar el registro
    if st.sidebar.button("Buscar"):
        resultados = buscar_por_dni(dni)
        if len(resultados) > 0:
            df = pd.DataFrame(resultados, columns=["id", "Dni", "NombreJuicio", "NumerodeExpte", "RadicacionJudicial",
                                                   "NumeroOficio", "NumeroExpteAdministrativo", "MedidaCautelar",
                                                   "AclaracionCautelar", "FechaInicio", "FechaFin", "Observacion",
                                                   "MontoEmbargo", "Sanciones", "NominacionRadicacion", "Juzgado"])
            st.dataframe(df)
        else:
            st.write("No se encontraron registros con el DNI especificado.")

    # Sección para actualizar un campo del registro
    id = st.text_input("Ingrese el ID del registro que desea actualizar")
    campo = st.selectbox("Seleccione el campo a actualizar", ['NombreJuicio', 'NumerodeExpte', 'RadicacionJudicial',
                                                            'NumeroOficio', 'NumeroExpteAdministrativo', 'MedidaCautelar',
                                                            'AclaracionCautelar', 'FechaInicio', 'FechaFin', 'Observacion',
                                                            'Sanciones', 'MontoEmbargo','NominacionRadicacion', 'Juzgado'])
    valor = st.text_input("Ingrese el nuevo valor")

    if st.button("Guardar"):
        registros_actualizados = actualizar_registro(id, campo, valor)
        ver_modificacion = buscar_por_id(id)
        df = pd.DataFrame(ver_modificacion, columns=["id", "Dni", "NombreJuicio", "NumerodeExpte", "RadicacionJudicial",
                                                   "NumeroOficio", "NumeroExpteAdministrativo", "MedidaCautelar",
                                                   "AclaracionCautelar", "FechaInicio", "FechaFin", "Observacion",
                                                   "MontoEmbargo", "Sanciones", "NominacionRadicacion", "Juzgado"])
        st.dataframe(df)

        if registros_actualizados > 0:
            st.info("Se actualizó correctamente el registro.")
        else:
            st.warning("No se pudo actualizar el registro.")

    # Cierre de la conexión a la base de datos
    conn.close()
