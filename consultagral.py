import streamlit as st
import sqlite3
import pandas as pd
import base64
from io import BytesIO


# Conexión a la base de datos SQLite
conn = sqlite3.connect('embargos.db')
c = conn.cursor()

# Función para ejecutar una consulta SQL y obtener los resultados como un DataFrame
def run_query(query):
    c.execute(query)
    data = c.fetchall()
    columns = [description[0] for description in c.description]
    df = pd.DataFrame(data, columns=columns)
    df['Cantidad de Registros'] = len(df)  # Agregar una columna con la cantidad de registros
    return df
def get_all_juicios():
    query = "SELECT * FROM Juicios"
    return run_query(query)

# Consulta los registros filtrados por el número de expediente
def get_juicios_by_expediente(numero_expediente):
    query = f"SELECT * FROM Juicios WHERE NumerodeExpte = {numero_expediente}"
    df = run_query(query)
    df['Cantidad de Registros'] = len(df)  # Actualizar la columna con la cantidad de registros
    return df


# Consulta los registros filtrados por el juzgado
def get_juicios_by_juzgado(juzgado):
    query = f"SELECT * FROM Juicios WHERE Juzgado = '{juzgado}'"
    df = run_query(query)
    df['Cantidad de Registros'] = len(df)  # Actualizar la columna con la cantidad de registros
    return df

# Consulta los registros filtrados por la localidad del juzgado
def get_juicios_by_localidad(localidades):
    localidades = "','".join(localidades)
    query = f"SELECT * FROM Juicios WHERE Juzgado IN (SELECT Localidad FROM Juzgados WHERE Localidad IN ('{localidades}'))"
    df = run_query(query)
    df['Cantidad de Registros'] = len(df)  # Actualizar la columna con la cantidad de registros
    return df

# Consulta los registros filtrados por fecha de inicio
def get_juicios_by_fecha_inicio(fecha_inicio):
    query = f"SELECT * FROM Juicios WHERE FechaInicio = '{fecha_inicio}'"
    df = run_query(query)
    df['Cantidad de Registros'] = len(df)  # Actualizar la columna con la cantidad de registros
    return df

# Consulta los registros filtrados por fecha de fin
def get_juicios_by_fecha_fin(fecha_fin):
    query = f"SELECT * FROM Juicios WHERE FechaFin = '{fecha_fin}'"
    df = run_query(query)
    df['Cantidad de Registros'] = len(df)  # Actualizar la columna con la cantidad de registros
    return df

# Consulta los registros filtrados entre dos fechas de inicio
def get_juicios_between_fechas_inicio(fecha_inicio_1, fecha_inicio_2):
    query = f"SELECT * FROM Juicios WHERE FechaInicio BETWEEN '{fecha_inicio_1}' AND '{fecha_inicio_2}'"
    df = run_query(query)
    df['Cantidad de Registros'] = len(df)  # Actualizar la columna con la cantidad de registros
    return df

# Consulta los registros filtrados entre dos fechas de fin
def get_juicios_between_fechas_fin(fecha_fin_1, fecha_fin_2):
    query = f"SELECT * FROM Juicios WHERE FechaFin BETWEEN '{fecha_fin_1}' AND '{fecha_fin_2}'"
    df = run_query(query)
    df['Cantidad de Registros'] = len(df)  # Actualizar la columna con la cantidad de registros
    return df

# Función para generar un enlace de descarga en formato Excel
def download_link(df, filename):
    excel_data = BytesIO()
    with pd.ExcelWriter(excel_data, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    excel_data.seek(0)
    b64 = base64.b64encode(excel_data.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}.xlsx">Descargar Excel</a>'
    return href


LOGO_IMAGE = "./imagenes/justice.png"

st.markdown(
    """
    <style>
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
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
       <p class="logo-text" style="text-align: center;">Juicios-Embargos</p>


    </div>
    """,
    unsafe_allow_html=True
)

if "ingreso" not in st.session_state:
    st.session_state.ingreso = ""


if st.session_state.ingreso == "":
    st.warning("Por favor Ingrese Correctamente")
 

else :
    # Página principal
    def main():
       
        

        # Obtener todos los juicios
        juicios = get_all_juicios()

        # Mostrar los juicios en una tabla
        # st.title('Juicios Registrados')
        
        st.markdown(
        f"""
        <div style='text-align: left'>
            <h1 style='color: black;'>Juicios Registrados</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
        # st.dataframe(juicios)

        # Opciones de filtrado
        st.sidebar.title('Filtrar Juicios')

        # Filtrar por número de expediente
        numero_expediente = st.sidebar.text_input('Número de Expediente')
        if st.sidebar.button('Filtrar por Expediente'):
            juicios_filtrados = get_juicios_by_expediente(numero_expediente)
            st.subheader(f'Juicios filtrados por Número de Expediente: {numero_expediente}')
            st.dataframe(juicios_filtrados)
            st.write("CANTIDAD DE REGISTROS :  " + str(len(juicios_filtrados)))
            st.markdown(download_link(juicios_filtrados, 'juicios_filtrados_por_expediente'), unsafe_allow_html=True)

        # Filtrar por localidad del juzgado
        localidades = st.sidebar.multiselect('Localidad del Juzgado', ('Capital', 'Concepcion', 'Banda Rio Sali', 'Monteros', 'Penales'))
        if st.sidebar.button('Filtrar por Localidad del Juzgado'):
            juicios_filtrados = get_juicios_by_localidad(localidades)
            st.subheader(f'Juicios filtrados por Localidad del Juzgado: {", ".join(localidades)}')
            st.dataframe(juicios_filtrados)
            st.write("CANTIDAD DE REGISTROS :  " + str(len(juicios_filtrados)))
            st.markdown(download_link(juicios_filtrados, 'juicios_filtrados_por_localidad_juzgado'), unsafe_allow_html=True)

        # Filtrar por fecha de inicio
        fecha_inicio = st.sidebar.date_input('Fecha de Inicio')
        if st.sidebar.button('Filtrar por Fecha de Inicio'):
            juicios_filtrados = get_juicios_by_fecha_inicio(fecha_inicio)
            st.subheader(f'Juicios filtrados por Fecha de Inicio: {fecha_inicio}')
            st.dataframe(juicios_filtrados)
            st.write("CANTIDAD DE REGISTROS :  " + str(len(juicios_filtrados)))
            st.markdown(download_link(juicios_filtrados, 'juicios_filtrados_por_fecha_inicio'), unsafe_allow_html=True)

        # Filtrar por fecha de fin
        fecha_fin = st.sidebar.date_input('Fecha de Fin')
        if st.sidebar.button('Filtrar por Fecha de Fin'):
            juicios_filtrados = get_juicios_by_fecha_fin(fecha_fin)
            st.subheader(f'Juicios filtrados por Fecha de Fin: {fecha_fin}')
            st.dataframe(juicios_filtrados)
            st.write("CANTIDAD DE REGISTROS :  " + str(len(juicios_filtrados)))
            st.markdown(download_link(juicios_filtrados, 'juicios_filtrados_por_fecha_fin'), unsafe_allow_html=True)

        # Filtrar entre dos fechas de inicio
        fecha_inicio_1 = st.sidebar.date_input('Fecha de Inicio 1')
        fecha_inicio_2 = st.sidebar.date_input('Fecha de Inicio 2')
        if st.sidebar.button('Filtrar entre Fechas de Inicio'):
            juicios_filtrados = get_juicios_between_fechas_inicio(fecha_inicio_1, fecha_inicio_2)
            st.subheader(f'Juicios filtrados entre Fechas de Inicio: {fecha_inicio_1} y {fecha_inicio_2}')
            st.dataframe(juicios_filtrados)
            st.write("CANTIDAD DE REGISTROS :  " + str(len(juicios_filtrados)))
            st.markdown(download_link(juicios_filtrados, 'juicios_filtrados_entre_fechas_inicio'), unsafe_allow_html=True)

        # Filtrar entre dos fechas de fin
        fecha_fin_1 = st.sidebar.date_input('Fecha de Fin 1')
        fecha_fin_2 = st.sidebar.date_input('Fecha de Fin 2')
        if st.sidebar.button('Filtrar entre Fechas de Fin'):
            juicios_filtrados = get_juicios_between_fechas_fin(fecha_fin_1, fecha_fin_2)
            st.subheader(f'Juicios filtrados entre Fechas de Fin: {fecha_fin_1} y {fecha_fin_2}')
            st.dataframe(juicios_filtrados)
            st.write("CANTIDAD DE REGISTROS :  " + str(len(juicios_filtrados)))
            st.markdown(download_link(juicios_filtrados, 'juicios_filtrados_entre_fechas_fin'), unsafe_allow_html=True)

    # Ejecutar la aplicación
    if __name__ == '__main__':
        main()
