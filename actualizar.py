import sqlite3
import streamlit as st
import pandas as pd

# Conexión a la base de datos SQLite
conn = sqlite3.connect('embargos.db')
c = conn.cursor()
hide_streamlit_style = """
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
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# Función para buscar juicios por DNI
def buscar_por_dni(dni):
    c.execute("SELECT * FROM Juicios WHERE Dni=?", (dni,))
    return c.fetchall()

# Función para actualizar un campo en un juicio
def actualizar_campo(id_juicio, campo, valor):
    c.execute(f"UPDATE Juicios SET {campo}=? WHERE id=?", (valor, id_juicio))
    conn.commit()

# Configuración de la aplicación Streamlit
st.title('Modificacion Valores Juicios')

# Control para buscar por DNI
dni_busqueda = st.text_input('Buscar por DNI')
if st.button('Buscar'):
    juicios_encontrados = buscar_por_dni(dni_busqueda)
    if juicios_encontrados:
        # Convertir la lista de resultados a un DataFrame
        df = pd.DataFrame(juicios_encontrados, columns=['ID', 'Dni', 'NombreJuicio', 'NumerodeExpte', 'RadicacionJudicial',
                                                        'NumeroOficio', 'NumeroExpteAdministrativo', 'MedidaCautelar',
                                                        'AclaracionCautelar', 'FechaInicio', 'FechaFin', 'Observacion',
                                                        'Sanciones', 'MontoEmbargo','NominacionRadicacion', 'Juzgado'])

        st.dataframe(df)
        for juicio in juicios_encontrados:
            st.write('---')
            # Control para modificar cada campo del juicio
            for i, campo in enumerate(juicio[2:], start=2):
                nuevo_valor = st.text_input(f'{df.columns[i]}:', value=campo, key=f'campo_{i}')
                if st.button(f'Actualizar {df.columns[i]}', key=f'boton_{i}'):  # Asignar claves únicas a los widgets
                    actualizar_campo(juicio[0], df.columns[i], nuevo_valor)
    else:
        st.write('No se encontraron juicios para el DNI especificado.')

# Cierre de la conexión a la base de datos
conn.close()
